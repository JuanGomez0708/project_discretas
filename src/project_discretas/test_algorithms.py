from project_discretas.utils import load_files
from project_discretas.algorithms import is_connected, has_cycle, is_tree, is_forest

for i in range (1,7):
    file_name=f"ejemplo_{i}.csv"
    print(f"\nPrueba {file_name}")
    g=load_files(file_name, is_directed=False)
    is_connected(g)
    has_cycle(g)
    is_tree(g)
    is_forest(g)