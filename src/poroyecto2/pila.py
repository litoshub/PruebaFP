'''
Created on 11 nov 2024

@author: carlo
'''

from typing import Generic, TypeVar
from poroyecto2 import agrgado_lineal
E = TypeVar('E')

class Pila(agrgado_lineal[E]):
    def _init_(self):
        super()._init_()

    def of(self) -> 'Pila[E]':
 
        return Pila()

    def push(self, element: E):
        self._elements.append(element)

    def pop(self) -> E:
        if self.is_empty:
            raise IndexError("No se puede eliminar de una pila vacía.")
        return self._elements.pop()

    def top(self) -> E:
        if self.is_empty:
            raise IndexError("No se puede obtener el elemento de una pila vacía.")
        return self._elements[-1]