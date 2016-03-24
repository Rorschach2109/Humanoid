from HumanoidAPI.MorphologyEnum import MorphologyEnum
from HumanoidOperations import EnlargeOperation, MorphologyOperation, ThresholdOperation, ContourOperation, \
    CannyOperation, HorizontalRemovalOperation, VericalRemovalOperation, HistogramEqualizationOperation, \
    GaussianBlurOperation, OtsuThresholdOperation, ConvertToGrayOperation
from HumanoidCheckers import CheckerManager

from functools import wraps


def update_history(func):
    @wraps(func)
    def update_history_wrapper(bridge, *args):
        result = func(bridge, *args)
        bridge.image_history.append(result)
        return result
    return update_history_wrapper

class OperationsBridge(object):
    def __init__(self, original_image):
        self._convert_to_gray_operation = ConvertToGrayOperation.ConvertToGrayOperation()
        self._enlarge_operation = EnlargeOperation.EnlargeOperation()

        self._morphology_operation = MorphologyOperation.MorphologyOperation()

        self._threshold_operation = ThresholdOperation.ThresholdOperation()
        self._otsu_threshold_operation = OtsuThresholdOperation.OtsuThresholdOperation()

        self._contour_operation = ContourOperation.ContourOperation()
        self._canny_operation = CannyOperation.CannyOperation()

        self._horizontal_removal_operation = HorizontalRemovalOperation.HorizontalRemovalOperation()
        self._vertical_removal_operation = VericalRemovalOperation.VerticalRemovalOperation()

        self._histogram_equalization_operation = HistogramEqualizationOperation.HistogramEqualization()

        self._gaussian_blur_operation = GaussianBlurOperation.GaussianBlurOperation()

        self.image_history = [(original_image, 'Original')]

    @update_history
    def convert_to_gray(self, image):
        return self._convert_to_gray_operation.run_operation(image=image)

    @update_history
    def enlarge_image(self, image, fx, fy):
        return self._enlarge_operation.run_operation(image=image, fx=fx, fy=fy)

    @update_history
    def morph_image(self, image, op_type, kernel, iterations=1):
        if MorphologyEnum.valid_enum(op_type):
            return self._morphology_operation.run_operation(image=image, op_type=op_type,
                                                            kernel=kernel, iterations=iterations)

    @update_history
    @CheckerManager.negative_check
    def thresh_image(self, image, inverse, bottom_boundary):
        return self._threshold_operation.run_operation(image=image, bottom_boundary=bottom_boundary, inverse=inverse)

    @update_history
    @CheckerManager.negative_check
    def otsu_thresh_image(self, image):
        return self._otsu_threshold_operation.run_operation(image=image)

    @update_history
    def find_contours(self, image):
        return self._contour_operation.run_operation(image=image)

    @update_history
    def canny_operation(self, image):
        return self._canny_operation.run_operation(image=image)

    @update_history
    def horizontal_line_removal(self, image, remove_max_size=2):
        return self._horizontal_removal_operation.run_operation(image=image, remove_max_size=remove_max_size)

    @update_history
    def vertical_line_removal(self, image, remove_max_size=2):
        return self._vertical_removal_operation.run_operation(image=image, remove_max_size=remove_max_size)

    @update_history
    def histogram_equalization(self, image):
        return self._histogram_equalization_operation.run_operation(image=image)

    @update_history
    def gaussian_blur(self, image, mask=(3, 3)):
        return self._gaussian_blur_operation.run_operation(image=image, mask=mask)
