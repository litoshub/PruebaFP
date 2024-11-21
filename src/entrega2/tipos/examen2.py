'''
Created on 21 nov 2024

@author: carlo
'''
from entrega2.tipos.Agregado_lineal import AgregadoLineal

class ColaConLimite(AgregadoLineal):
    def __init__(self, capacidad: int):
        """Constructor que inicializa la cola con una capacidad máxima."""
        super().__init__()
        self.capacidad = capacidad

    @staticmethod
    def of(capacidad: int):
        """Método de factoría para crear una instancia de ColaConLimite."""
        return ColaConLimite(capacidad)

    def add(self, e):
        """Añade un elemento a la cola si no está llena. Lanza OverflowError si está llena."""
        if self.is_full():
            raise OverflowError("La cola está llena.")
        self._elements.append(e)

    def is_full(self) -> bool:
        """Verifica si la cola ha alcanzado su capacidad máxima."""
        return self.size >= self.capacidad

    def __repr__(self):
        return f"ColaConLimite(capacidad={self.capacidad}, elementos={self._elements})"
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
        """Añade un elemento al agregado."""
        self._elements.append(e)

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

# Subclase concreta para pruebas
class AgregadoLinealConcreto(AgregadoLineal):
    def add(self, e: E) -> None:
        """Implementación del método add en la subclase concreta."""
        self._elements.append(e)

   
    
# Pruebas para AgregadoLineal
def test_agregado_lineal():
    print("TEST DE AGREGADO LINEAL:")

    # 1. Prueba de `add` y `add_all`
    agregado = AgregadoLinealConcreto()
    # Añadir números pares e impares
    agregado.add_all([10, 20, 30, 40, 50, 11, 15, 19, 21])
    print(f"Agregado después de añadir elementos: {agregado}")
    assert agregado.size == 9, "El tamaño debería ser 9."

    # 2. Prueba de `contains`
    assert agregado.contains(30) == True, "El agregado debe contener el 30."
    assert agregado.contains(60) == False, "El agregado no debe contener el 60."

    # 3. Prueba de `find`
    assert agregado.find(lambda x: x > 25) == 30, "El primer elemento mayor que 25 debería ser 30."
    assert agregado.find(lambda x: x > 60) == None, "No debe encontrar un elemento mayor que 60."

    # 4. Prueba de `filter` (Filtrar números pares)
    result_pares = agregado.filter(lambda x: x % 2 == 0)
    print(f"Elementos filtrados (pares): {result_pares}")
    

    # 5. Prueba de `filter` (Filtrar números impares)
    result_impares = agregado.filter(lambda x: x % 2 != 0)
    print(f"Elementos filtrados (impares): {result_impares}")
    

    # 6. Prueba de `remove` y `remove_all`
    removed = agregado.remove()
    print(f"Elemento removido: {removed}")
    
    
    removed_all = agregado.remove_all()
    print(f"Elementos removidos: {removed_all}")
    

    print("Pruebas de AgregadoLineal pasadas exitosamente.\n")

# Pruebas para ColaConLimite
def test_cola_con_limite():
    print("TEST DE COLA CON LÍMITE:")

    # 1. Crear cola con capacidad limitada
    cola = ColaConLimite.of(3)
    cola.add("Tarea 1")
    cola.add("Tarea 2")
    cola.add("Tarea 3")

    # Verificar si la cola está llena
    assert cola.is_full() == True, "La cola debería estar llena."
    
    # Intentar añadir un cuarto elemento
    try:
        cola.add("Tarea 4")
    except OverflowError as e:
        print(e)  # Debería imprimir: "La cola está llena."
    else:
        assert False, "Se esperaba un OverflowError."

    # 2. Eliminar elementos
    removed = cola.remove()
    print(f"Elemento removido: {removed}")
    assert removed == "Tarea 1", "El primer elemento removido debería ser 'Tarea 1'."

    # 3. Verificar el estado después de remover un elemento
    print(f"Estado de la cola después de la remoción: {cola}")
    assert cola.size == 2, "El tamaño de la cola debería ser 2 después de remover un elemento."

    # 4. Verificar que la cola no está llena después de remover
    assert cola.is_full() == False, "La cola no debería estar llena después de remover un elemento."

    # 5. Probar remoción de todos los elementos
    cola.remove_all()
    print(f"Estado de la cola después de remover todos los elementos: {cola}")
    assert cola.is_empty == True, "La cola debería estar vacía después de remover todos los elementos."

    print("Pruebas de ColaConLimite pasadas exitosamente.\n")


# Ejecutar todas las pruebas
if __name__ == '__main__':
    test_agregado_lineal()
    test_cola_con_limite()
    
    
    
