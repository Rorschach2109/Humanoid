from HumanoidOperations.Operation import Operation

import cv2 as cv

class HistogramEqualization(Operation):
    def __init__(self):
        super(HistogramEqualization, self).__init__('HistEq')

    def run_operation(self, **kwargs):
        super(HistogramEqualization, self).run_operation(**kwargs)



        return cv.equalizeHist(self._image), self._operation_name
