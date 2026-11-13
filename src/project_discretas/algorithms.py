from project_discretas.graphs import Graph

def _check_connected(graph: Graph) -> bool:
    nodes = graph.get_nodes()
    if not nodes:
        return True 

    visited = set()
    stack = [nodes[0]]

    while stack:
        current_node = stack.pop()
        if current_node not in visited:
            visited.add(current_node)
            for neighbor, _ in graph.get_neighbors(current_node):
                if neighbor not in visited:
                    stack.append(neighbor)

    return len(visited) == len(nodes)

def _check_cycle(graph:Graph) ->bool:
    visited=set()

    def dfs(node: str, parent: str)-> bool:
        visited.add(node)
        for neighbor, _ in graph.get_neighbors(node):
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False
    for node in graph.get_nodes():
        if node not in visited:
            if dfs(node, None):
                return True
    return False

# points 6-9

def is_connected(graph: Graph) -> bool:
    result = _check_connected(graph)
    print(f"is_connected: {result}")
    return result

def has_cycle(graph: Graph) -> bool:
    result = _check_cycle(graph)
    print(f"has_cycle: {result}")
    return result

def is_tree(graph: Graph) -> bool:
    result = _check_connected(graph) and not _check_cycle(graph)
    print(f"is_tree: {result}")
    return result

def is_forest(graph: Graph) -> bool:
    result = not _check_cycle(graph)
    print(f"is_forest: {result}")
    return result