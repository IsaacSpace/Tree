

class Tree:
    def __init__(self):
        self.edges = []
        self.nodes = []
    
    def add_node(self, node_name):
        self.nodes.append(node_name)

    def remove_node(self, node_name):
        self.nodes.remove(node_name)