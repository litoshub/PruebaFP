'''
Created on 20 nov 2024

@author: carlo
'''
from typing import List, TypeVar, Generic

E = TypeVar('E')
P = TypeVar('P')

class ColaDePrioridad(Generic[E, P]):
    def __init__(self):
        self._elements: List[E] = []
        self._priorities: List[P] = []

    @property
    def size(self) -> int:
        return len(self._elements)

    @property
    def is_empty(self) -> bool:
        return self.size == 0

    def elements(self) -> List[E]:
        return self._elements

    def add(self, e: E, priority: P) -> None:
        index = self.__index_order(priority)
        self._elements.insert(index, e)
        self._priorities.insert(index, priority)

    def __index_order(self, priority: P) -> int:
        for i, p in enumerate(self._priorities):
            if priority < p:
                return i
        return len(self._priorities)

    def remove(self) -> E:
        assert self.size > 0, 'El agregado está vacío'
        self._priorities.pop(0)
        return self._elements.pop(0)

    def remove_all(self) -> List[E]:
        result = []
        while not self.is_empty:
            result.append(self.remove())
        return result

    def decrease_priority(self, e: E, new_priority: P) -> None:
        if e in self._elements:
            index = self._elements.index(e)
            self._elements.pop(index)
            self._priorities.pop(index)
            self.add(e, new_priority)

    def __repr__(self):
        return f"ColaPrioridad({list(zip(self._elements, self._priorities))})"
