from HumanoidOperations.Operation import Operation

import cv2 as cv

class EnlargeOperation(Operation):
    def __init__(self):
        super(EnlargeOperation, self).__init__(self.__class__.__name__)
        self.image_history = []

    def run_operation(self, **kwargs):
        super(EnlargeOperation, self).run_operation(**kwargs)

        fx = kwargs['fx']
        fy = kwargs['fy']

        return cv.resize(self._image, None, fx=fx, fy=fy, interpolation=cv.INTER_CUBIC)
