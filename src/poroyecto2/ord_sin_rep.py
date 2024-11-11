'''
Created on 11 nov 2024

@author: carlo
'''
from typing import Callable, Generic, List, TypeVar
from poroyecto2 import agrgado_lineal
E = TypeVar('E')
R = TypeVar('R')

class ListaOrdenadaSinRepeticion(agrgado_lineal[E]):
    def _init_(self, order: Callable[[E], R]):
        super()._init_()
        self._order = order

    def of(self, order: Callable[[E], R])-> 'ListaOrdenadaSinRepeticion[E]':
        return ListaOrdenadaSinRepeticion(order)

    def add(self, element: E):
        if element not in self._elements:  
            self._elements.append(element)
            self._elements.sort(key=self._order)

    def remove(self) -> E:
        if self.is_empty:
            raise IndexError("No se puede eliminar de una lista vacía.")
        return self._elements.pop(0)