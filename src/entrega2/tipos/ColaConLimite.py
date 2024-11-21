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

# Ejemplo de uso
if __name__ == '__main__':
    # Crear una cola con capacidad máxima de 3 elementos
    cola = ColaConLimite.of(3)

    # Añadir tareas
    cola.add("Tarea 1")
    cola.add("Tarea 2")
    cola.add("Tarea 3")

    # Intentar añadir un cuarto elemento
    try:
        cola.add("Tarea 4")  # Esto debe lanzar OverflowError
    except OverflowError as e:
        print(e)  # Debe imprimir: "La cola está llena."

    # Eliminar un elemento de la cola
    print(cola.remove())  # Debe imprimir: 'Tarea 1'
