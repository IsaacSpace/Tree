

class Tree:
    def __init__(self):
        self.edges = set()
        self.nodes = set()
    
    def add_node(self, node_name):
        self.nodes.add(node_name)

    def remove_node(self, node_name):
        self.nodes.remove(node_name)

    def add_edge(self, init_node, end_node, weight = None):
        if(init_node not in self.nodes or end_node not in self.nodes):
            print("Init or end node are not in the nodes set.")
            exit()
        self.edges.add((init_node, end_node, weight))


# usage example

t = Tree()
t.add_node("A")
t.add_node("B")

t.add_edge("A", "B")


print(t.nodes)
print(t.edges)