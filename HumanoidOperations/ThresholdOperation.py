from HumanoidOperations.Operation import Operation

import cv2 as cv

class ThresholdOperation(Operation):
    def __init__(self):
        super(ThresholdOperation, self).__init__(self.__class__.__name__)

    def run_operation(self, **kwargs):
        super(ThresholdOperation, self).run_operation(**kwargs)

        threshold_bottom_boundary = kwargs['bottom_boundary']
        inverse = kwargs['inverse']

        ret, thresh = cv.threshold(self._image, threshold_bottom_boundary, 255,
                                   cv.THRESH_BINARY_INV if inverse else cv.THRESH_BINARY)

        return thresh, self._operation_name
