from cluster import Cluster
from code_gen_decorators import StackBase, dec_generate 


class ClusterStack(Stack):
    def __init__(self):
        super(self, ClusterStack).__init__(Cluster(), 'config_records.py')

    @dec_generate()
    def generate(self):
        pass


if __name__ == '__main__':
    stack = ClusterStack()
    clusters = stack.generate().generated()
    for cluster in clusters:
        print(cluster)
