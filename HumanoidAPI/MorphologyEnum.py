class MorphologyEnum(object):

    MIN = -1
    EROSION = 0
    DILATION = 1
    OPENING = 2
    CLOSING = 3
    MAX = CLOSING + 1

    @staticmethod
    def valid_enum(value):
        return value in range(MorphologyEnum.MIN + 1, MorphologyEnum.MAX)
