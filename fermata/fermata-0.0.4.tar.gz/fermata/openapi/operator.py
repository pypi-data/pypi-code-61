from .. import loader
from ..exception import BadOperationId


def default_operation_id(path_exception, operation):
    terms, by, use_by = [], [], False
    for part in path_exception.split('/'):
        if len(part) > 2 and part[0] == '{' and part[-1] == '}':
            by.append(part[1:-1])
            use_by = True
        elif part:
            terms.append(part)
            by.append('')
    if use_by:
        operation = '_'.join([operation, 'by'] + by)
    operation_id = '.'.join([''] + terms + [operation])
    return operation_id


class Operator:

    def __init__(self, operation_id, default_package=None):
        if default_package and operation_id.startswith('.'):
            operation_id = default_package + operation_id
        self.operation_id = operation_id

    def load(self):
        self.operate = loader.load(self.operation_id)
        return self

    def operate(self, request, **kwargs):
        return self.load().operate(request, **kwargs)

    def __call__(self, request, **kwargs):
        return self.operate(request, **kwargs)
