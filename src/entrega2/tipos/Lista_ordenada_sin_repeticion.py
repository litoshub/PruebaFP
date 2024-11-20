'''
Created on 20 nov 2024

@author: carlo
'''
from .Lista_ordenada import ListaOrdenada
from typing import Callable, TypeVar, Generic

E = TypeVar('E')
R = TypeVar('R')

class ListaOrdenadaSinRepeticion(ListaOrdenada[E, R], Generic[E, R]):
    def add(self, e: E) -> None:
        if e not in self._elements:
            super().add(e)

    @staticmethod
    def of(order: Callable[[E], R]):
        return ListaOrdenadaSinRepeticion(order)

    def __repr__(self):
        return f"ListaOrdenadaSinRepeticion({self._elements})"
