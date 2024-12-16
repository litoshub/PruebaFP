'''
Created on 16 dic 2024

@author: carlo
'''
from __future__ import annotations
from typing import TypeVar, Generic, Set, Optional
from entrega3.grafo import Grafo

V = TypeVar('V')
E = TypeVar('E')

class E_Grafo(Grafo[V, E]):
    def __init__(self, es_dirigido: bool = True):
        super().__init__(es_dirigido)

    def __add_neighbors(self, source: V, target: V) -> None:
        """Añade un vértice al conjunto de vecinos de otro vértice"""
        if source not in self.adyacencias:
            self.adyacencias[source] = {}

    def __add_predecessors(self, source: V, target: V) -> None:
        """Añade un vértice al conjunto de predecesores de otro vértice"""
        if target not in self.adyacencias:
            self.adyacencias[target] = {}

    def add_edge(self, source: V, target: V, edge: E) -> bool:
        """Añade una arista entre dos vértices"""
        if source == target or not (source in self.vertex_set() and target in self.vertex_set()):
            return False

        if self.contains_edge(source, target):
            return False

        self.__add_neighbors(source, target)
        self.__add_predecessors(source, target)
        self.adyacencias[source][target] = edge

        if not self.es_dirigido:
            self.adyacencias[target][source] = edge

        return True

    def edge_weight(self, source: V, target: V) -> Optional[E]:
        """Devuelve el peso de la arista entre dos vértices"""
        if source in self.adyacencias and target in self.adyacencias[source]:
            return self.adyacencias[source][target]
        return None

    def add_vertex(self, vertex: V) -> bool:
        """Añade un nuevo vértice al grafo"""
        if vertex in self.vertex_set():
            return False
        self.adyacencias[vertex] = {}
        return True

    def edge_source(self, edge: E) -> Optional[V]:
        """Devuelve el vértice origen de una arista"""
        for source in self.adyacencias:
            for target, e in self.adyacencias[source].items():
                if e == edge:
                    return source
        return None

    def edge_target(self, edge: E) -> Optional[V]:
        """Devuelve el vértice destino de una arista"""
        for source in self.adyacencias:
            for target, e in self.adyacencias[source].items():
                if e == edge:
                    return target
        return None

    def vertex_set(self) -> Set[V]:
        """Devuelve el conjunto de vértices del grafo"""
        return set(self.adyacencias.keys())

    def contains_edge(self, source: V, target: V) -> bool:
        """Verifica si existe una arista entre dos vértices"""
        return source in self.adyacencias and target in self.adyacencias[source]

    def predecessors(self, vertex: V) -> Set[V]:
        """Devuelve los predecesores de un vértice"""
        if not self.es_dirigido:
            return set(self.adyacencias[vertex].keys()) if vertex in self.adyacencias else set()
        
        preds = set()
        for v in self.adyacencias:
            if vertex in self.adyacencias[v]:
                preds.add(v)
        return preds

    def successors(self, vertex: V, forward: bool = True) -> Set[V]:
        """Devuelve los sucesores de un vértice según el tipo de recorrido"""
        if forward:
            return set(self.adyacencias[vertex].keys()) if vertex in self.adyacencias else set()
        return self.predecessors(vertex)

    def inverse_graph(self) -> E_Grafo[V, E]:
        """Genera el grafo inverso"""
        if not self.es_dirigido:
            return self

        inverse = E_Grafo[V, E](True)
        for vertex in self.vertex_set():
            inverse.add_vertex(vertex)

        for source in self.adyacencias:
            for target, edge in self.adyacencias[source].items():
                inverse.add_edge(target, source, edge)

        return inverse