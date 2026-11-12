class Graph:
    def __init__(self, is_directed: bool = False):
        self.is_directed = is_directed
        self.adj_list = {}

    def add_node(self,node: str):
        if node not in self.adj_list:
            self.adj_list[node] = []

    def add_edge(self, source: str, target: str, weight: float = 1.0):
        self.add_node(source)
        self.add_node(target)
        self.adj_list[source].append((target, weight))
        if not self.is_directed:
            self.adj_list[target].append((source, weight))
    def get_nodes(self):
        return list(self.adj_list.keys())

    def get_neighbors(self,node: str):
        return self.adj_list.get(node, [])