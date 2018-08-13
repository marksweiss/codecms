from cluster import Cluster
from code_gen_decorators import StackBase, dec_generate
import os


class ClusterStack(StackBase):
    def __init__(self):
        super(ClusterStack, self).__init__(Cluster(), 'config_records.py')

    @dec_generate
    def generate(self):
        pass


if __name__ == '__main__':
    stack = ClusterStack()
    stack.generate()
    for cluster in stack.generated:
        print(cluster)
