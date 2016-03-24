from HumanoidAPI.MorphologyEnum import MorphologyEnum
from HumanoidOperations.Operation import Operation

import cv2 as cv

class MorphologyOperation(Operation):
    def __init__(self):
        super(MorphologyOperation, self).__init__(self.__class__.__name__)

    def run_operation(self, **kwargs):
        super(MorphologyOperation, self).run_operation(**kwargs)

        operation_type = kwargs['op_type']
        kernel = kwargs['kernel']
        iterations = kwargs['iterations']

        if operation_type == MorphologyEnum.EROSION:
            return self._run_erosion(kernel, iterations)
        elif operation_type == MorphologyEnum.DILATION:
            return self._run_dilation(kernel, iterations)
        elif operation_type == MorphologyEnum.OPENING:
            return self._run_morphology_ex(cv.MORPH_OPEN, kernel)
        elif operation_type == MorphologyEnum.CLOSING:
            return self._run_morphology_ex(cv.MORPH_CLOSE, kernel)

    def _run_erosion(self, kernel, iterations):
        return cv.erode(self._image, kernel, iterations=iterations), self._operation_name + ' -> erosion'

    def _run_dilation(self, kernel, iterations):
        return cv.dilate(self._image, kernel, iterations=iterations), self._operation_name + ' -> dilation'

    def _run_morphology_ex(self, op_type, kernel):
        return cv.morphologyEx(self._image, op_type, kernel), self._operation_name + ' -> morphology_ex'
