'''
Created on 20 nov 2024

@author: carlo
'''
from .Agregado_lineal import AgregadoLineal
from typing import Callable, TypeVar, Generic

E = TypeVar('E')
R = TypeVar('R')

class ListaOrdenada(AgregadoLineal[E], Generic[E, R]):
    def __init__(self, order: Callable[[E], R]):
        super().__init__()
        self._order = order

    @staticmethod
    def of(order: Callable[[E], R]):
        return ListaOrdenada(order)

    def __index_order(self, e: E) -> int:
        for i, elem in enumerate(self._elements):
            if self._order(e) < self._order(elem):
                return i
        return len(self._elements)

    def add(self, e: E) -> None:
        index = self.__index_order(e)
        self._elements.insert(index, e)

    def __repr__(self):
        return f"ListaOrdenada({self._elements})"
