from typing import Generic, List, TypeVar, Tuple
from poroyecto2 import agrgado_lineal

E = TypeVar('E')
P = TypeVar('P')

class ColaPrioridad(agrgado_lineal[E]):
    def _init_(self):
        super()._init_()
        self._priorities: List[P] = []  

    def priorities(self) -> List[P]:
        return self._priorities

    def add(self, element: E, priority: P):

        self._elements.append(element)
        self._priorities.append(priority)

        combined = sorted(zip(self._priorities, self._elements), key=lambda x: x[0], reverse=True)
        self._priorities, self._elements = zip(*combined) if combined else ([], [])
        self._priorities, self._elements = list(self._priorities), list(self._elements)

    def remove(self) -> E:

        if self.is_empty:
            raise IndexError("No se puede eliminar de una cola de prioridad vacía.")
        
        self._priorities.pop(0)
        return self._elements.pop(0)
  