from HumanoidAPI.ImageManager import ImageManager
from HumanoidOperations.Operation import Operation

class VerticalRemovalOperation(Operation):
    def __init__(self):
        super(VerticalRemovalOperation, self).__init__(self.__class__.__name__)

    def run_operation(self, **kwargs):
        super(VerticalRemovalOperation, self).run_operation(**kwargs)

        img_copy = ImageManager.copy_image(self._image)

        rows = img_copy.shape[0]
        cols = img_copy.shape[1]

        remove_max_size = kwargs['remove_max_size']

        for x in xrange(cols):
            start = (0, 0)
            end = (0, 0)
            start_flag = False

            for y in xrange(rows):
                if False == start_flag and img_copy[y][x] == 0:
                    start = (x, y)
                    start_flag = True
                elif True == start_flag and img_copy[y][x] != 0:
                    end = (x, y)
                    start_flag = False
                    VerticalRemovalOperation._remove_line(img_copy, start, end, remove_max_size)

        return img_copy, 'VertRemove'

    @staticmethod
    def _remove_line(image, start, end, remove_max_size, fill_color=255):
        start_x, start_y = start
        end_x, end_y = end
        size = end_y - start_y + 1

        if size < remove_max_size:
            for row_index in xrange(start_y, end_y + 1):
                image[row_index][start_x] = fill_color
