import os
from project_discretas.graphs import Graph

def load_files(file_name:str,is_directed: bool = False) -> Graph:
    graph = Graph(is_directed=is_directed)

    current_dir = os.path.dirname(os.path.abspath(__file__)) #src   
    file_path = os.path.join(current_dir, file_name)
    if not os.path.isabs(file_name) and not os.path.exists(file_name):
        file_path = os.path.join(root_dir, file_name)
    else:
        file_path = file_name   

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith("source"):  
                continue
            
            parts = line.split(",")
            if len(parts) >= 3:
                source = parts[0].strip()
                target = parts[1].strip()
                try:
                    weight = float(parts[2].strip())
                except ValueError:
                    continue

                graph.add_edge(source, target, weight)
    return graph