import os

os.environ['DARKNET_PATH'] = os.environ.get('DARKNET_PATH', './darknet')
from darknet import darknet

from darknet.darknet import c_int, pointer, predict_image, \
    get_network_boxes, free_detections, do_nms_sort, remove_negatives


def detect_image(network, class_names, image, thresh=.5, hier_thresh=.5, nms=.45):
    """
    Detect objects for an image with a given network.
    Unlike the original function it doesn't call `decode_detection`.
    """
    pnum = pointer(c_int(0))
    predict_image(network, image)
    detections = get_network_boxes(network, image.w, image.h,
                                   thresh, hier_thresh, None, 0, pnum, 0)
    num = pnum[0]
    if nms:
        do_nms_sort(detections, num, len(class_names), nms)
    predictions = remove_negatives(detections, class_names, num)

    free_detections(detections, num)
    return sorted(predictions, key=lambda x: x[1])


class NN:
    def __init__(self,
                 config,
                 data_file,
                 weights, batch_size):
        self.network, self.class_names, self.class_colors = darknet.load_network(
            config,
            data_file,
            weights,
            batch_size=batch_size
        )

    def detect(self, darknet_image, thresh):
        if isinstance(darknet_image, DNImage):
            darknet_image = darknet_image.img()
        return detect_image(self.network, self.class_names, darknet_image, thresh=thresh)


class DNImage:
    def __init__(self, w, h):
        self.w, self.h = w, h
        self._img = None

    def __enter__(self):
        self._img = darknet.make_image(self.w, self.h, 3)
        return self

    def img(self):
        if self._img is None:
            raise ValueError("darknet image is not initialized")
        return self._img

    def copy_from(self, img):
        darknet.copy_image_from_bytes(self.img(), img.tobytes())

    def __exit__(self, type, value, traceback):
        darknet.free_image(self._img)
        self._img = None
