from cluster import Cluster
from code_gen_decorators import StackBase, dec_generate
import os


class ClusterStack(StackBase):
    def __init__(self):
        path = os.path.dirname(os.path.realpath(__file__))
        config_records_file = 'config_records.py'
        config_records_path = os.path.join(path, config_records_file)
        super(ClusterStack, self).__init__(Cluster(), config_records_path)

    # TODO ABCMeta, put this in base class NotImplemented
    @dec_generate
    def generate(self):
        pass

if __name__ == '__main__':
    stack = ClusterStack()
    stack.generate()
    for cluster in stack.generated:
        print(cluster)
