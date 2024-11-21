'''
Created on 20 nov 2024

@author: carlo
'''
from typing import List, TypeVar, Generic, Callable
from abc import ABC, abstractmethod

E = TypeVar('E')

class AgregadoLineal(ABC, Generic[E]):
    def __init__(self):
        self._elements: List[E] = []

    @property
    def size(self) -> int:
        return len(self._elements)

    @property
    def is_empty(self) -> bool:
        return self.size == 0

    @property
    def elements(self) -> List[E]:
        return list(self._elements)

    @abstractmethod
    def add(self, e: E) -> None:
         self._elements.append(e)

    def add_all(self, ls: List[E]) -> None:
        for item in ls:
            self.add(item)

    def remove(self) -> E:
        assert self.size > 0, 'El agregado está vacío'
        return self._elements.pop(0)

    def remove_all(self) -> List[E]:
        removed_elements = []
        while not self.is_empty:
            removed_elements.append(self.remove())
        return removed_elements
