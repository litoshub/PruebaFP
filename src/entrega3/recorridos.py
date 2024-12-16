

from typing import TypeVar, List, Set
from entrega3.grafo import Grafo
from entrega2.tipos.Cola import Cola
from entrega2.tipos.Pila import Pila

V = TypeVar('V')  # Tipo de los vértices
E = TypeVar('E')  # Tipo de las aristas

def bfs(grafo: Grafo[V, E], inicio: V, destino: V) -> List[V]:
    """
    Realiza un recorrido en anchura (BFS) desde un vértice inicial hasta un vértice destino usando una Cola.
    
    :param grafo: Grafo sobre el que realizar la búsqueda.
    :param inicio: Vértice inicial.
    :param destino: Vértice de destino.
    :return: Lista de vértices en el camino más corto desde inicio a destino, o [] si no hay camino.
    """
    visitados = set()
    cola = Cola()
    cola.encolar(inicio)
    predecesores = {inicio: None}

    while not cola.esta_vacia():
        vertice = cola.desencolar()

        if vertice == destino:
            break

        if vertice not in visitados:
            visitados.add(vertice)

            for vecino in grafo.successors(vertice):
                if vecino not in visitados:
                    cola.encolar(vecino)
                    predecesores[vecino] = vertice

    return reconstruir_camino(predecesores, destino)

def dfs(grafo: Grafo[V, E], inicio: V, destino: V) -> List[V]:
    """
    Realiza un recorrido en profundidad (DFS) desde un vértice inicial hasta un vértice destino usando una Pila.
    
    :param grafo: Grafo sobre el que realizar la búsqueda.
    :param inicio: Vértice inicial.
    :param destino: Vértice de destino.
    :return: Lista de vértices en el camino más corto desde inicio a destino, o [] si no hay camino.
    """
    visitados = set()
    pila = Pila()
    pila.apilar(inicio)
    predecesores = {inicio: None}

    while not pila.esta_vacia():
        vertice = pila.desapilar()

        if vertice == destino:
            break

        if vertice not in visitados:
            visitados.add(vertice)

            # Recorremos los vecinos en orden inverso para mantener el orden original del DFS
            for vecino in reversed(list(grafo.successors(vertice))):
                if vecino not in visitados:
                    pila.apilar(vecino)
                    predecesores[vecino] = vertice

    return reconstruir_camino(predecesores, destino)

def reconstruir_camino(predecesores: dict, destino: V) -> List[V]:
    """
    Reconstruye el camino desde el origen hasta el destino usando el diccionario de predecesores.
    
    :param predecesores: Diccionario que mapea cada vértice a su predecesor.
    :param destino: Vértice de destino.
    :return: Lista de vértices en el camino desde el origen hasta el destino.
    """
    camino = []
    vertice_actual = destino

    # Si el destino no está en los predecesores, no hay camino
    if destino not in predecesores:
        return []

    while vertice_actual is not None:
        camino.insert(0, vertice_actual)
        vertice_actual = predecesores.get(vertice_actual)

    return camino
