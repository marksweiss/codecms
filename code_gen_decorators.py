from copy import deepcopy
from functools import wraps


def StackBase(object):
    def __init__(self, prototype, config_records):
        self.prototype = prototype
        self.config_records = config_records
        self.generated = []


def dec_generate(generate_func):
    @wraps(generate_func)
    def wrapper(self):
        for config_record in self.config_records:
           instance = deepcopy(self.prototype)
           for attr_name, attr_val in config_record.items():
               setattr(instance, attr_name, attr_val)
           self.generated.append(deepcopy(self.prototype))
    return wrapper

