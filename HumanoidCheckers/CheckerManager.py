from functools import wraps

def negative_check(func):
    @wraps(func)
    def negative_check_wrapper(bridge, image, *args):
        image, operation_name = func(bridge, image, *args)

        pixel_map = {0: 0, 255: 0}

        height = image.shape[0]
        width = image.shape[1]

        for y in xrange(height):
            for x in xrange(width):
                pixel_map[image[y][x]] += 1

        if pixel_map[0] > pixel_map[255]:
            image = ~image

        return image, operation_name

    return negative_check_wrapper
