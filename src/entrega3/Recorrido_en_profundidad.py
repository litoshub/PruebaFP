'''
Created on 16 dic 2024

@author: carlo
'''
'''
Created on 21 nov 2024

@author: damat
'''
from typing import TypeVar, Generic, Dict, Set, Optional, List
from abc import ABC, abstractmethod
from entrega3.grafo import Grafo
from entrega2.tipos.Cola import Cola
from entrega2.tipos.Pila import Pila
from entrega3.Recorrido import Recorrido

V = TypeVar('V')
E = TypeVar('E')

class Recorrido_en_profundidad(Recorrido[V, E]):
    @staticmethod
    def of(grafo: Grafo[V, E]) -> Recorrido[V, E]:
        """
        Método de factoría para crear una nueva instancia.
        """
        return Recorrido_en_profundidad(grafo)

    def traverse(self, source: V) -> None:
        """
        Realiza un recorrido en profundidad (DFS) del grafo.
        """
        visitados: Set[V] = set()
        pila = Pila()
        pila.apilar(source)
        self._tree[source] = (None, 0.0)
        
        while not pila.esta_vacia():
            vertice = pila.desapilar()
            
            if vertice not in visitados:
                visitados.add(vertice)
                self._path.append(vertice)
                
                for vecino in reversed(list(self._grafo.successors(vertice))):
                    if vecino not in visitados:
                        pila.apilar(vecino)
                        costo_arista = self._grafo.edge_weight(vertice, vecino) or 0.0
                        costo_acumulado = self._tree[vertice][1] + float(costo_arista)
                        self._tree[vecino] = (vertice, costo_acumulado)

# ... (resto de funciones bfs, dfs, etc.)