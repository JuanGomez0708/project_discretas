Para armar el grafo usamos un diccionario de lista de adyacencia, 
donde cada nodo guarda una lista con sus vecinos y el peso con sus conexiones.

Decidimos hacerlo así porque es fácil de entender,usar el diccionario
con listas es intuitivo para ir guardando los vecinos de cada nodo.
-No requiere un gran uso de memoria ya que los datos de los grafos están
guardados en cada csv y su utilización en algotithms es fácil.
-Cuando necesitamos revisar si el grafo está conectado o si tiene ciclos, es muy rápido pedirle a cada nodo únicamente sus vecinos directos.

¿Como nos fue?

Al comenzar nos costó un poco conectar todo, sobre todo como lograr que el programa encontrara bien los archivos csv en las carpetas y manejar los datos cuando los nodos venían con su peso. También tuvimos que corregir un par de detalles en la lógica para que el recorrido no se detuviera antes de buscar los buscar ciclos.

El usar varios archivos como (graphs, utils y algorithms) nos ayudó a encontrar los errores rápido y dejar todo funcionando bien con los ejemplos de prueba.