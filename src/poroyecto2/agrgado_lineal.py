'''
Created on 5 nov 2024

@author: carlo

elements, de tipo List[E] protegida: Esta propiedad será una lista que almacenará los elementos
añadidos.
• size(self) -> int, derivada: Indica el número de elementos en el agregado.
• is_empty(self) -> bool, derivada: Devuelve True si el agregado no tiene elementos y False en caso
contrario.
• elements(self) -> list[E], derivada: Devuelve la lista completa de elementos almacenados en el
agregado.
'''
from abc import ABC, abstractmethod
from typing import Generic, List, TypeVar

E = TypeVar('E')

class AgregadoLineal(ABC, Generic[E]):
    def __init__(self):
        # Propiedad protegida para almacenar los elementos
        self._elements: List[E] = []

    @property
    def size(self) -> int:
        """Devuelve el número de elementos en el agregado."""
        return len(self._elements)

    @property
    def is_empty(self) -> bool:
        """Devuelve True si el agregado está vacío, False en caso contrario."""
        return len(self._elements) == 0

    @property
    def elements(self) -> List[E]:
        """Devuelve una lista con todos los elementos almacenados en el agregado."""
        return self._elements

    @abstractmethod
    def add(self, e: E) -> None:
        """Método abstracto para añadir un nuevo elemento al agregado."""
        pass

    def add_all(self, ls: List[E]) -> None:
        """Añade una lista de elementos al agregado usando el método add."""
        for element in ls:
            self.add(element)

    def remove(self) -> E:
        """
        Elimina y devuelve el primer elemento agregado.
        Si el agregado está vacío, se lanza una excepción con un mensaje de error.
        """
        assert len(self._elements) > 0, 'El agregado está vacío'
        return self._elements.pop(0)

    def remove_all(self) -> List[E]:
        """
        Elimina y devuelve todos los elementos del agregado.
        Reutiliza is_empty() y remove() para eliminar los elementos de forma secuencial.
        """
        removed_elements = []
        while not self.is_empty:
            removed_elements.append(self.remove())
        return removed_elements


    
        
        