'''
Created on 20 nov 2024

@author: carlo
'''
from .Agregado_lineal import AgregadoLineal
from typing import TypeVar

E = TypeVar('E')

class Cola(AgregadoLineal[E]):
    @staticmethod
    def of():
        return Cola()

    def add(self, e: E) -> None:
        self._elements.append(e)

    def __repr__(self):
        return f"Cola({self._elements})"
