# Matemáticas Discretas II - Proyecto del Semestre (Entrega 1)

**Integrantes:**
- Juan Gómez (`JuanGomez0708`)
- Dirley Vanessa Britto (`VanessaBrittoM`)

---

## Implementación de Grafos escogida
Para armar el grafo usamos un **diccionario de listas de adyacencia**, donde cada nodo funciona como llave y guarda una lista con sus vecinos y el peso de sus conexiones.

Decidimos hacerlo así por las siguientes razones:
- **Facilidad e intuición:** Usar un diccionario con listas es muy intuitivo para ir guardando y consultando los vecinos de cada nodo.
- **Eficiencia de memoria:** No requiere un gran uso de memoria, ya que solo almacena las conexiones existentes cargadas desde cada archivo `.csv` y su utilización en `algorithms.py` es muy directa.
- **Velocidad en recorridos:** Cuando necesitamos revisar si el grafo es conexo o si tiene ciclos, es muy rápido pedirle a cada nodo únicamente sus vecinos directos.

## ¿Cómo nos fue?
Al comenzar nos costó un poco conectar todo, sobre todo lograr que el programa encontrara bien los archivos `.csv` en las carpetas y manejar los datos cuando los nodos venían con su peso. También tuvimos que corregir un par de detalles en la lógica para que el recorrido no se detuviera antes de buscar los ciclos.

Dividir el proyecto en varios módulos (`graphs.py`, `utils.py` y `algorithms.py`) nos ayudó a encontrar los errores rápido y dejar todo funcionando bien con los ejemplos de prueba.

## Ejecución del proyecto
Para probar el funcionamiento del código, ejecuta el siguiente comando en la terminal dentro de la carpeta raíz del proyecto:

```bash
uv run python -m project_discretas.test_algorithms