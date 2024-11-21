'''
Created on 21 nov 2024

@author: carlo
'''
from typing import List, TypeVar, Callable, Optional

E = TypeVar('E')

class AgregadoLineal:
    def __init__(self):
        """Constructor que inicializa una lista vacía para almacenar los elementos."""
        self._elements: List[E] = []

    @property
    def size(self) -> int:
        """Devuelve el número de elementos en el agregado."""
        return len(self._elements)

    @property
    def is_empty(self) -> bool:
        """Devuelve True si el agregado está vacío, False en caso contrario."""
        return self.size == 0

    @property
    def elements(self) -> List[E]:
        """Devuelve la lista completa de elementos almacenados en el agregado."""
        return list(self._elements)

    def add(self, e: E) -> None:
        self._elements.append(e)
        """Método abstracto para añadir un elemento. Debe ser implementado en subclases."""
            

    def add_all(self, ls: List[E]) -> None:
        """Añade todos los elementos de una lista al agregado utilizando el método add."""
        for item in ls:
            self.add(item)

    def remove(self) -> E:
        """Elimina y devuelve el primer elemento del agregado."""
        if self.is_empty:
            raise ValueError("El agregado está vacío")
        return self._elements.pop(0)

    def remove_all(self) -> List[E]:
        """Elimina todos los elementos del agregado y los devuelve."""
        removed_elements = []
        while not self.is_empty:
            removed_elements.append(self.remove())
        return removed_elements

    def contains(self, e: E) -> bool:
        """Verifica si un elemento está presente en el agregado."""
        return e in self._elements
   
    def find(self, func: Callable[[E], bool]) -> Optional[E]:
        """Devuelve el primer elemento que cumple con la condición dada por func."""
        for element in self._elements:
            if func(element):
                return element
        return None

    def filter(self, func: Callable[[E], bool]) -> List[E]:
        """Filtra los elementos del agregado según la función dada y devuelve una lista de los que cumplen la condición."""
        return [element for element in self._elements if func(element)]

    def __repr__(self):
        return f"AgregadoLineal({self._elements})"
    
    # Crear un AgregadoLineal y añadir algunos elementos
agregado = AgregadoLineal()
agregado.add_all([10, 20, 30, 40, 50])

# Verificar si un elemento está en el agregado
print(agregado.contains(30))  # True
print(agregado.contains(60))  # False

# Encontrar un elemento que cumpla una condición
print(agregado.find(lambda x: x > 25))  # 30 (primer elemento que cumple la condición)

# Filtrar elementos que cumplan una condición
print(agregado.filter(lambda x: x % 2 == 0))  # [10, 20, 30, 40, 50] (elementos pares)

