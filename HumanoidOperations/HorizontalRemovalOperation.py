from HumanoidAPI.ImageManager import ImageManager
from HumanoidOperations.Operation import Operation

class HorizontalRemovalOperation(Operation):
    def __init__(self):
        super(HorizontalRemovalOperation, self).__init__(self.__class__.__name__)

    def run_operation(self, **kwargs):
        super(HorizontalRemovalOperation, self).run_operation(**kwargs)

        img_copy = ImageManager.copy_image(self._image)

        rows = img_copy.shape[0]
        cols = img_copy.shape[1]

        remove_max_size = kwargs['remove_max_size']

        for y in xrange(rows):
            start = (0, 0)
            end = (0, 0)
            start_flag = False

            for x in xrange(cols):
                if False == start_flag and img_copy[y][x] == 0:
                    start = (y, x)
                    start_flag = True
                elif True == start_flag and img_copy[y][x] != 0:
                    end = (y, x)
                    start_flag = False
                    HorizontalRemovalOperation._remove_line(img_copy, start, end, remove_max_size)

        return img_copy, 'HorRemoval'

    @staticmethod
    def _remove_line(image, start, end, remove_max_size, fill_color=255):
        start_y, start_x = start
        end_y, end_x = end
        size = end_x - start_x + 1

        if size < remove_max_size:
            for column_index in xrange(start_x, end_x + 1):
                image[start_y][column_index] = fill_color
