'''
Created on 20 nov 2024

@author: carlo
'''
from .Agregado_lineal import AgregadoLineal
from typing import TypeVar

E = TypeVar('E')

class Pila(AgregadoLineal[E]):
    @staticmethod
    def of():
        return Pila()

    def add(self, e: E) -> None:
        self._elements.insert(0, e)

    def __repr__(self):
        return f"Pila({self._elements})"
