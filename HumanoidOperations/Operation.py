class Operation(object):

    def __init__(self, operation_name):
        self._operation_name = operation_name
        self._image = None

    def run_operation(self, **kwargs):
        print 'Running operation: %s' % self._operation_name
        self._image = kwargs['image']

    def operation_name(self):
        return self._operation_name
