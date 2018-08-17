class Cluster(object):
    def __init__(self):
        self.name = None
        self.number_of_nodes = 0
        self.node_type = None
        self.region = None

    def __repr__(self):
        return (f'Name: {self.name}\n'
                f'Number of Nodes: {self.number_of_nodes}\n'
                f'Node Type: {self.node_type}\n'
                f'Region: {self.region}\n')

