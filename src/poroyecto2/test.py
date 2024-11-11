'''
Created on 11 nov 2024

@author: carlo
'''
from typing import Callable, TypeVar, List
from poroyecto2 import agrgado_lineal  # Suponiendo que esta es la ubicación correcta de AgregadoLineal

E = TypeVar('E')
R = TypeVar('R')

class ListaOrdenada(agrgado_lineal[E]):
    def __init__(self, order: Callable[[E], R]):
        super().__init__()
        self._order = order

    @staticmethod
    def of(order: Callable[[E], R]) -> 'ListaOrdenada[E]':
        return ListaOrdenada(order)

    def add(self, element: E):
        # Añade el elemento y ordena la lista
        self._elements.append(element)
        self._elements.sort(key=self._order)

    def remove(self) -> E:
        # Elimina y retorna el primer elemento si la lista no está vacía
        if self.is_empty():
            raise IndexError("No se puede eliminar de una lista vacía.")
        return self._elements.pop(0)

    def remove_all(self) -> List[E]:
        # Elimina y retorna todos los elementos en orden
        removed_elements = []
        while not self.is_empty():
            removed_elements.append(self.remove())
        return removed_elements

    def __repr__(self) -> str:
        return f"ListaOrdenada({self._elements})"

# Pruebas de funcionamiento
# Crear una lista ordenada con el criterio lambda x: x
lista = ListaOrdenada.of(lambda x: x)

# Añadir los elementos 3, 1, y 2 en este orden
lista.add(3)
lista.add(1)
lista.add(2)
print("Resultado de la lista:", lista)

# Eliminar el primer elemento con `remove()`
elemento_eliminado = lista.remove()
print("################################################")
print("El elemento eliminado al utilizar remove():", elemento_eliminado)
print("################################################")

# Eliminar todos los elementos con `remove_all()`
elementos_eliminados = lista.remove_all()
print("Elementos eliminados utilizando remove_all:", elementos_eliminados)
print("################################################")

# Comprobando si se añaden los números en la posición correcta
lista.add(0)
print("Lista después de añadirle el 0:", lista)
lista.add(10)
print("Lista después de añadirle el 10:", lista)
lista.add(7)
print("Lista después de añadirle el 7:", lista)
