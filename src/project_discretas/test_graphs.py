from project_discretas.graphs import Graph

# point 3
print("PRUEBA GRAFO NO DIRIGIDO")
undirected_g = Graph(is_directed=False)
undirected_g.add_edge("A", "B", 4.0)

print("Nodos:", undirected_g.get_nodes())
print("Vecinos de A:", undirected_g.get_neighbors("A"))
print("Vecinos de B:", undirected_g.get_neighbors("B"))

# point 4
print("PRUEBA GRAFO DIRIGIDO")
directed_g = Graph(is_directed=True)
directed_g.add_edge("A", "B", 4.0)

print("Nodos:", directed_g.get_nodes())
print("Vecinos de A:", directed_g.get_neighbors("A"))
print("Vecinos de B:", directed_g.get_neighbors("B"))