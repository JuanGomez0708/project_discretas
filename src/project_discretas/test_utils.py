from project_discretas.utils import load_files

print("Pueba csv")
graph=load_files("ejemplo_1.csv", is_directed=False)

print("Nodos:", graph.get_nodes())
if graph.get_nodes():
    first_node = graph.get_nodes()[0]
    print(f"Vecinos de {first_node}:", graph.get_neighbors(first_node))
          