from HumanoidOperations.Operation import Operation

import cv2 as cv

class GaussianBlurOperation(Operation):
    def __init__(self):
        super(GaussianBlurOperation, self).__init__('GausBlur')

    def run_operation(self, **kwargs):
        super(GaussianBlurOperation, self).run_operation(**kwargs)

        mask = kwargs['mask']

        return cv.GaussianBlur(self._image, mask, 0), self._operation_name
