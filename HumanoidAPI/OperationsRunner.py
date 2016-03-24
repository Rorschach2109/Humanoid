from HumanoidAPI.ImageManager import ImageManager
from HumanoidAPI.MorphologyEnum import MorphologyEnum
from HumanoidAPI.OperationsBridge import OperationsBridge

class OperationsRunner(object):
    def __init__(self):
        self._operations = list()

        self.CONVERT_TO_GRAY = [OperationsBridge.convert_to_gray]

        self.ENLARGE = [OperationsBridge.enlarge_image]

        self.THRESH_BINARY = [OperationsBridge.thresh_image, False]
        self.THRESH_BINARY_INV = [OperationsBridge.thresh_image, True]
        self.THRESH_OTSU_BINARY = [OperationsBridge.otsu_thresh_image]

        self.OPENING = [OperationsBridge.morph_image, MorphologyEnum.OPENING]
        self.CLOSING = [OperationsBridge.morph_image, MorphologyEnum.CLOSING]
        self.DILATION = [OperationsBridge.morph_image, MorphologyEnum.DILATION]
        self.EROSION = [OperationsBridge.morph_image, MorphologyEnum.EROSION]

        self.CONTOUR = [OperationsBridge.find_contours]
        self.CANNY = [OperationsBridge.canny_operation]

        self.HORIZONTAL_REMOVAL = [OperationsBridge.horizontal_line_removal]
        self.VERTICAL_REMOVAL = [OperationsBridge.vertical_line_removal]

        self.HISTOGRAM_EQUALIZATION = [OperationsBridge.histogram_equalization]

        self.GAUSSIAN_BLUR = [OperationsBridge.gaussian_blur]

        self._bridge = None

    def add_operation(self, defined_operation, *args):
        result = [x for x in defined_operation]
        result.extend(args)
        self._operations.append(result)

    def run_operations(self, image):
        self._bridge = OperationsBridge(image)
        for args in self._operations:
            operation = args[0]
            image = operation(self._bridge, image, *args[1:])[0]
            #ImageManager.display_image(image, '1')

    def get_image_history(self):
        return self._bridge.image_history
