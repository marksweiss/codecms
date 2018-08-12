class Cluster(object):
    def __init__(self):
        self.name = None
        self.number_of_nodes = 0
        self.node_type = None
        self.region = None

    def __repr__(self):
        return ('Name: {self.name}\n'
                'Number of Nodes: {self.number_of_nodes}\n'
                'Node Type: {self.node_type}\n'
                'Region: {self.region}\n')

