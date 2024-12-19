

'''
Created on 21 nov 2024

@author: damat
'''
from typing import TypeVar, Generic, Dict, Set, Optional, List
from abc import ABC, abstractmethod
from entrega3.grafo import Grafo
from entrega2.tipos.Cola import Cola
from entrega2.tipos.Pila import Pila

V = TypeVar('V')
E = TypeVar('E')

class Recorrido(ABC, Generic[V, E]):
    def __init__(self, grafo: Grafo[V, E]):
        self._tree: Dict[V, tuple[Optional[V], float]] = {}
        self._path: List[V] = []
        self._grafo = grafo

    def path_to_origin(self, vertex: V) -> List[V]:
        if vertex not in self._tree:
            return []
        
        path = []
        current = vertex
        
        while current is not None:
            path.append(current)
            current = self._tree[current][0]
            
        return list(reversed(path))

    def origin(self, vertex: V) -> Optional[V]:
        if vertex not in self._tree:
            return None
            
        current = vertex
        while self._tree[current][0] is not None:
            current = self._tree[current][0]
            
        return current

    def groups(self) -> Dict[V, Set[V]]:
        result: Dict[V, Set[V]] = {}
        
        for vertex in self._tree:
            origin = self.origin(vertex)
            if origin is not None:
                if origin not in result:
                    result[origin] = set()
                result[origin].add(vertex)
                
        return result

    @abstractmethod
    def traverse(self, source: V) -> None:
        pass

# ... (mantener todas las importaciones y código anterior igual)

def bfs(grafo: Grafo[V, E], inicio: V, destino: V) -> List[V]:
    """
    Realiza un recorrido en anchura (BFS) desde un vértice inicial hasta un vértice destino.
    """
    visitados = set()
    cola = Cola()
    cola.add(inicio)
    predecesores = {inicio: None}

    while not cola.is_empty:  # Cambiado: is_empty es una propiedad, no un método
        vertice = cola.remove()  # Cambiado: usamos remove() en lugar de desencolar()

        if vertice == destino:
            break

        if vertice not in visitados:
            visitados.add(vertice)

            for vecino in grafo.successors(vertice):
                if vecino not in visitados:
                    cola.add(vecino)
                    predecesores[vecino] = vertice

    return reconstruir_camino(predecesores, destino)

# ... (mantener el resto del código igual)

    return reconstruir_camino(predecesores, destino)

def dfs(grafo: Grafo[V, E], inicio: V, destino: V) -> List[V]:
    """
    Realiza un recorrido en profundidad (DFS) desde un vértice inicial hasta un vértice destino.
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

            for vecino in reversed(list(grafo.successors(vertice))):
                if vecino not in visitados:
                    pila.apilar(vecino)
                    predecesores[vecino] = vertice

    return reconstruir_camino(predecesores, destino)

def reconstruir_camino(predecesores: dict, destino: V) -> List[V]:
    """
    Reconstruye el camino desde el origen hasta el destino usando el diccionario de predecesores.
    """
    camino = []
    vertice_actual = destino

    if destino not in predecesores:
        return []

    while vertice_actual is not None:
        camino.insert(0, vertice_actual)
        vertice_actual = predecesores.get(vertice_actual)

    return camino
