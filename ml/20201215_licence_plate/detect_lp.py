import json
import sys
import cv2
import numpy as np
import argparse
from simplebbox.array import xyxy_abs_to_rel, xyxy_rel_to_abs_int, cxcywh_to_x0y0wh_trunc_int, \
    cxcywh_to_x0y0x1y1_trunc_int

from darknet_facade import NN, DNImage
from pathlib import Path
from skimage.io import imread, imsave


def labels_list_param(string):
    return string.split(',')


def parse_args(argv):
    parser = argparse.ArgumentParser("licence plate detector")
    parser.add_argument("-i", "--input-dir", help="input directory", required=True)
    parser.add_argument("-o", "--output-dir", default="output", help="output directory", required=False)
    parser.add_argument("-V", "--verbose", action='store_true', help="verbose output", required=False)

    parser.add_argument("--vehicle-weights", default="data/yolov4.weights",
                        help="yolo weights path for vehicle detector")
    parser.add_argument("--vehicle-config", default="cfg/yolov4.cfg",
                        help="path to config file for vehicle detector")
    parser.add_argument("--vehicle-data-file", default="cfg/coco.data",
                        help="path to data file for vehicle detector")
    parser.add_argument("--vehicle-thresh", type=float, default=.35,
                        help="remove vehicle detections with confidence below this value")
    parser.add_argument("--vehicle-labels", type=labels_list_param, default="car,truck,bus,motorbike",
                        help="comma separated list of classes considered as vehicles "
                             "(no spaces between the class names)")

    parser.add_argument("--lp-weights", default="data/_yolov4-custom_best.weights",
                        help="yolo weights path for licence plate detector")
    parser.add_argument("--lp-config", default="data/_yolov4-custom_inference.cfg",
                        help="path to config file for licence plate detector")
    parser.add_argument("--lp-data-file", default="data/obj.data",
                        help="path to data file for licence plate detector")
    parser.add_argument("--lp-thresh", type=float, default=.35,
                        help="remove licence plate detections with confidence below this value")

    return parser.parse_args(argv)


def draw_boxes(detections, image, colors):
    import cv2
    for label, confidence, bbox in detections:
        left, top, right, bottom = cxcywh_to_x0y0x1y1_trunc_int(bbox)
        cv2.rectangle(image, (left, top), (right, bottom), colors[label], 1)
        cv2.putText(image, "{} [{:.2f}]".format(label, float(confidence)),
                    (left, top - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    colors[label], 2)
    return image


def save_vis(img, detections, path_out, class_colors):
    show = draw_boxes(detections, img.copy(), class_colors)
    imsave(path_out, show)


def transform_bbox(cxcywh, det_size, car_bbox_ltwh):
    cx, cy, w, h = xyxy_rel_to_abs_int(xyxy_abs_to_rel(cxcywh, det_size), car_bbox_ltwh[2:4])
    return cx + car_bbox_ltwh[0], cy + car_bbox_ltwh[1], w, h


def transform_detections(detections, src_size, src_bbox_ltwh):
    return [
        (label, confidence, transform_bbox(cxcywh, src_size, src_bbox_ltwh)) for (label, confidence, cxcywh) in
        detections
    ]


def save_detections_as_json(path, detections):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w") as f:
        json.dump(detections, f)


def main(argv):
    args = parse_args(argv)
    verbose = args.verbose
    input_path = Path(args.input_dir)
    in_paths = sorted([p for p in input_path.glob("*.jpg") if p.is_file()])
    print(in_paths)
    if len(in_paths) == 0:
        print(f"no files found in {input_path}")
        exit(1)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    nn_vehicles = NN(
        args.vehicle_config,
        args.vehicle_data_file,
        args.vehicle_weights,
        batch_size=1
    )

    nn_lp = NN(
        args.lp_config,
        args.lp_data_file,
        args.lp_weights,
        batch_size=1
    )

    w_lp, h_lp = 416, 416

    for in_path in in_paths:
        img = imread(str(in_path))
        height, width = img.shape[:2]
        with DNImage(width, height) as dn_img:
            dn_img.copy_from(img)
            detections = nn_vehicles.detect(dn_img, thresh=args.vehicle_thresh)

        detections = [d for d in detections
                      if d[0] in args.vehicle_labels]
        save_detections_as_json(output_dir.joinpath("vehicles", in_path.name).with_suffix(".json"),
                                detections)

        if verbose:
            print(f"detected {len(detections)} vehicles")
            vis_path = output_dir.joinpath(in_path.name).with_suffix(".vis.jpg")
            save_vis(img, detections, vis_path, nn_vehicles.class_colors)

        detections_lp = detect_lp(detections, img, nn_lp, w_lp, h_lp, args.lp_thresh, verbose)
        save_detections_as_json(output_dir.joinpath("lp", in_path.name).with_suffix(".json"),
                                detections_lp)

        if verbose:
            vis_path = output_dir.joinpath(in_path.name).with_suffix(f".vis_lp.jpg")
            lst_lp_detections = sum(detections_lp.values(), [])
            save_vis(img, lst_lp_detections, vis_path, nn_lp.class_colors)


def detect_lp(detections, img, network_lp, w_lp, h_lp, lp_thresh, verbose):
    detections_lp_all = {}
    with DNImage(w_lp, h_lp) as dn_img_lp:
        for i, (label, confidence, bbox) in enumerate(detections):
            img_car = crop_bbox(img, bbox)
            img_car_resized = cv2.resize(img_car, (w_lp, h_lp))
            dn_img_lp.copy_from(img_car_resized)
            detections_lp = network_lp.detect(dn_img_lp, thresh=lp_thresh)
            if verbose:
                print(f"for vehicle {i} - {label} found {len(detections_lp)} licence plates")
            bbox_ltwh = cxcywh_to_x0y0wh_trunc_int(bbox)
            detections_lp_all[i] = transform_detections(detections_lp, src_size=(w_lp, h_lp), src_bbox_ltwh=bbox_ltwh)
    return detections_lp_all


def crop_bbox(img, bbox_cxcywh):
    height, width = img.shape[:2]
    left, top, right, bottom = cxcywh_to_x0y0x1y1_trunc_int(bbox_cxcywh)
    left = np.clip(left, 0, width - 1)
    right = np.clip(right, 0, width - 1)
    top = np.clip(top, 0, height - 1)
    bottom = np.clip(bottom, 0, height - 1)
    img_car = img[top: bottom, left: right]
    return img_car


if __name__ == '__main__':
    main(sys.argv[1:])
    exit(0)
