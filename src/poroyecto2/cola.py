'''
Created on 11 nov 2024

@author: carlo
'''
from typing import Generic, TypeVar
from poroyecto2 import agrgado_lineal
E = TypeVar('E')

class Cola(agrgado_lineal[E]):
    def _init_(self):
        super()._init_()

    def of(self) -> 'Cola[E]':
        return Cola()

    def add(self, element: E):
        self._elements.append(element)

    def remove(self) -> E:
        if self.is_empty:
            raise IndexError("No se puede eliminar de una cola vacía.")
        return self._elements.pop(0)
    