from HumanoidOperations.Operation import Operation

import cv2 as cv

class ConvertToGrayOperation(Operation):
    def __init__(self):
        super(ConvertToGrayOperation, self).__init__('Convert2Gray')

    def run_operation(self, **kwargs):
        super(ConvertToGrayOperation, self).run_operation(**kwargs)

        return cv.cvtColor(self._image, cv.COLOR_BGR2GRAY), self._operation_name
