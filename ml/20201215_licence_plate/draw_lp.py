import argparse
import json
import sys
from pathlib import Path

from simplebbox.array import cxcywh_to_x0y0x1y1_trunc_int
from skimage.io import imread, imsave

from darknet_facade import class_colors


def parse_args(argv):
    parser = argparse.ArgumentParser("licence plate detector")
    parser.add_argument("-i", "--input-dir", help="input directory", required=True)
    parser.add_argument("-o", "--output-dir", default="output", help="output directory", required=False)
    parser.add_argument("-V", "--verbose", action='store_true', help="verbose output", required=False)

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


def load_detections_from_json(path):
    path = Path(path)
    with path.open("r") as f:
        return json.load(f)


def main(argv):
    args = parse_args(argv)
    input_path = Path(args.input_dir)
    in_paths = sorted([p for p in input_path.glob("*.jpg") if p.is_file()])
    print(in_paths)
    if len(in_paths) == 0:
        print(f"no files found in {input_path}")
        exit(1)

    output_dir = Path(args.output_dir)
    classes = Path("./data/coco.names").open().read().splitlines()
    classes_lp = Path("./data/obj.names").open().read().splitlines()

    for in_path in in_paths:
        img = imread(str(in_path))

        detections = load_detections_from_json(output_dir.joinpath("vehicles", in_path.name).with_suffix(".json"))

        vis_path = output_dir.joinpath(in_path.name).with_suffix(".vis.jpg")
        save_vis(img, detections, vis_path, class_colors(classes))

        detections_lp = load_detections_from_json(output_dir.joinpath("lp", in_path.name).with_suffix(".json"))

        vis_path = output_dir.joinpath(in_path.name).with_suffix(f".vis_lp.jpg")
        lst_lp_detections = sum(detections_lp.values(), [])
        save_vis(img, lst_lp_detections, vis_path, class_colors(classes_lp))

        if args.verbose:
            print(f"detected {len(detections)} vehicles and {len(lst_lp_detections)} licence plates")


if __name__ == '__main__':
    main(sys.argv[1:])
    exit(0)
