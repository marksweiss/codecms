from copy import deepcopy
from functools import wraps
import imp
import os


class StackBase(object):
    def __init__(self, prototype, config_records_path):
        self.prototype = prototype

        _, config_records_file_name = os.path.split(config_records_path)
        config_records_module_name = os.path.splitext(config_records_file_name)[0]
        self.config_records = imp.load_source(config_records_module_name,
                                              config_records_path)

        self.generated = []


def dec_generate(generate_func):
    @wraps(generate_func)
    def wrapper(self):
        for config_record in self.config_records.RECORDS:
            instance = deepcopy(self.prototype)
            for attr_name, attr_val in config_record.items():
                setattr(instance, attr_name, attr_val)
            self.generated.append(instance)

            generate_func(self)
    return wrapper
