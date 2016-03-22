from HumanoidAPI.MorphologyEnum import MorphologyEnum
from HumanoidOperations import EnlargeOperation, MorphologyOperation, ThresholdOperation, ContourOperation, \
    CannyOperation

from functools import wraps


def update_history(func):
    @wraps(func)
    def wrapper(bridge, *args):
        result = func(bridge, *args)
        bridge.image_history.append(result)
        return result
    return wrapper

class OperationsBridge(object):
    def __init__(self, original_image):
        self._enlarge_operation = EnlargeOperation.EnlargeOperation()
        self._morphology_operation = MorphologyOperation.MorphologyOperation()
        self._threshold_operation = ThresholdOperation.ThresholdOperation()
        self._contour_operation = ContourOperation.ContourOperation()
        self._canny_operation = CannyOperation.CannyOperation()

        self.image_history = [original_image]

    @update_history
    def enlarge_image(self, image, fx, fy):
        return self._enlarge_operation.run_operation(image=image, fx=fx, fy=fy)

    @update_history
    def morph_image(self, image, op_type, kernel, iterations=1):
        if MorphologyEnum.valid_enum(op_type):
            return self._morphology_operation.run_operation(image=image, op_type=op_type,
                                                            kernel=kernel, iterations=iterations)

    @update_history
    def thresh_image(self, image, inverse, bottom_boundary):
        return self._threshold_operation.run_operation(image=image, bottom_boundary=bottom_boundary, inverse=inverse)

    @update_history
    def find_contours(self, image):
        return self._contour_operation.run_operation(image=image)

    @update_history
    def canny_operation(self, image):
        return self._canny_operation.run_operation(image=image)
