from copy import deepcopy
from functools import wraps


class StackBase(object):
    def __init__(self, prototype, config_records):
        self.prototype = prototype
        self.config_records = config_records
        self.generated = []


def dec_generate(generate_func):
    @wraps(generate_func)
    def wrapper(self):
        # Create a new Stack for each config_record
        # assigning it's attrs to the values in the config_record
        # for the key in the record matching the attr_name in the instance. 
        # The append the instance to self.generated

        # TODO DYNAMICALLY LOAD config_records HERE
        for config_record in self.config_records:
            instance = deepcopy(self.prototype)
            for attr_name, attr_val in config_record.items():
                setattr(instance, attr_name, attr_val)
            self.generated.append(instance)

            generate_func()
    return wrapper

