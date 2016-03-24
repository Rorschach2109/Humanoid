from HumanoidOperations.Operation import Operation

import cv2 as cv

class OtsuThresholdOperation(Operation):
    def __init__(self):
        super(OtsuThresholdOperation, self).__init__('Otsu')

    def run_operation(self, **kwargs):
        super(OtsuThresholdOperation, self).run_operation(**kwargs)

        ret, thresh = cv.threshold(self._image, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

        return thresh, self._operation_name
