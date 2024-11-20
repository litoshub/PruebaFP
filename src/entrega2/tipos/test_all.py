from entrega2.tipos.Lista_ordenada import ListaOrdenada

print("TEST DE LISTA ORDENADA:")

# Creación de una lista con criterio de orden lambda x: x

print("Creación de una lista con criterio de orden lambda x: x")
lista = ListaOrdenada.of(lambda x: x)
lista.add_all([3, 1, 2])
print(f"Se añade en este orden: 3, 1, 2")
print(f"Resultado de la lista: {lista}")  # ListaOrdenada([1, 2, 3])

# Eliminar el primer elemento

removed_element = lista.remove()
print(f"El elemento eliminado al utilizar remove(): {removed_element}")  # 1

# Eliminar todos los elementos

removed_elements = lista.remove_all()
print(f"Elementos eliminados utilizando remove_all: {removed_elements}")  # [1, 2, 3]

# Comprobación de inserción en orden correcto

print("Comprobando si se añaden los números en la posición correcta...")
lista.add_all([3, 1, 2])
lista.add(0)
print(f"Lista después de añadirle el 0: {lista}")  # ListaOrdenada([0, 1, 2, 3])
lista.add(10)
print(f"Lista después de añadirle el 10: {lista}")  # ListaOrdenada([0, 1, 2, 3, 10])
lista.add(7)
print(f"Lista después de añadirle el 7: {lista}")  # ListaOrdenada([0, 1, 2, 3, 7, 10])


from entrega2.tipos.Lista_ordenada_sin_repeticion import ListaOrdenadaSinRepeticion

print("TEST DE LISTA ORDENADA SIN REPETICIÓN:")

# Creación de una lista con criterio de orden lambda x: -x

print("Creación de una lista con criterio de orden lambda x: -x")
lista_sin_rep = ListaOrdenadaSinRepeticion.of(lambda x: -x)
lista_sin_rep.add_all([23, 47, 47, 1, 2, -3, 4, 5])
print(f"Se añade en este orden: 23, 47, 47, 1, 2, -3, 4, 5")
print(f"Resultado de la lista ordenada sin repetición: {lista_sin_rep}")  # ListaOrdenadaSinRepeticion([47, 23, 5, 4, 2, 1, -3])

# Eliminar el primer elemento

removed_element = lista_sin_rep.remove()
print(f"El elemento eliminado al utilizar remove(): {removed_element}")  # 47

# Eliminar todos los elementos

removed_elements = lista_sin_rep.remove_all()
print(f"Elementos eliminados utilizando remove_all: {removed_elements}")  # [47, 23, 5, 4, 2, 1, -3]

# Comprobación de inserción en orden correcto

print("Comprobando si se añaden los números en la posición correcta...")
lista_sin_rep.add_all([23, 47, 1, 2, -3, 4, 5])
lista_sin_rep.add(0)
print(f"Lista después de añadirle el 0: {lista_sin_rep}")  # ListaOrdenadaSinRepeticion([47, 23, 5, 4, 2, 1, 0, -3])
lista_sin_rep.add(0)  # No debería añadirlo, ya existe
print(f"Lista después de añadirle el 0: {lista_sin_rep}")  # ListaOrdenadaSinRepeticion([47, 23, 5, 4, 2, 1, 0, -3])
lista_sin_rep.add(7)
print(f"Lista después de añadirle el 7: {lista_sin_rep}")  # ListaOrdenadaSinRepeticion([47, 23, 7, 5, 4, 2, 1, 0, -3])


from entrega2.tipos.Cola import Cola

print("TEST DE COLA:")

# Creación de una cola vacía y añadir elementos

print("Creación de una cola vacía a la que luego se le añaden con un solo método los números: 23, 47, 1, 2, -3, 4, 5")
cola = Cola.of()
cola.add_all([23, 47, 1, 2, -3, 4, 5])
print(f"Resultado de la cola: {cola}")  # Cola([23, 47, 1, 2, -3, 4, 5])

# Eliminar todos los elementos

removed_elements = cola.remove_all()
print(f"Elementos eliminados utilizando remove_all: {removed_elements}")  # [23, 47, 1, 2, -3, 4, 5]


from entrega2.tipos.Cola_prioridad import ColaDePrioridad
print("TEST DE COLA PRIORIDAD")
def test_cola_prioridad():

    # Crear una cola de prioridad
    cola = ColaDePrioridad[str, int]()

    # Agregar pacientes con diferentes prioridades
    cola.add('Paciente A', 3)  # Dolor de cabeza leve
    cola.add('Paciente B', 2)  # Fractura en la pierna
    cola.add('Paciente C', 1)  # Ataque cardíaco

    # Verificar el estado de la cola
    assert cola.elements() == ['Paciente C', 'Paciente B', 'Paciente A'], "El orden de la cola es incorrecto."

    # Atender a los pacientes y verificar el orden de atención
    atencion = []
    while not cola.is_empty:
        atencion.append(cola.remove())

    assert atencion == ['Paciente C', 'Paciente B', 'Paciente A'], "El orden de atención no es correcto."
    print("Pruebas superadas exitosamente.")

if __name__ == '__main__':
    test_cola_prioridad()


