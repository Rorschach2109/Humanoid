from HumanoidOperations.Operation import Operation

import cv2 as cv

class CannyOperation(Operation):
    def __init__(self):
        super(CannyOperation, self).__init__(self.__class__.__name__)

    def run_operation(self, **kwargs):
        super(CannyOperation, self).run_operation(**kwargs)

        return cv.Canny(self._image, 100, 200, True)
