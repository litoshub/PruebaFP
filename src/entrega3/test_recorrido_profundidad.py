'''
Created on 16 dic 2024

@author: carlo
'''
from entrega3.red_social import Red_social
from entrega3.Usuario import Usuario
from entrega3.relacion import Relacion
from entrega2.tipos.Cola import Cola
from typing import List, Optional, Set

def dfs_modificado(grafo: Red_social, inicio: 'Usuario', destino: 'Usuario') -> Optional[List['Usuario']]:
    """
    Realiza un recorrido en profundidad (DFS) desde un vértice inicial hasta un vértice destino.
    """
    visitados = set()
    predecesores = {inicio: None}
    
    def dfs_recursivo(actual: 'Usuario') -> bool:
        visitados.add(actual)
        
        if actual == destino:
            return True
            
        for vecino in grafo.successors(actual):
            if vecino not in visitados:
                predecesores[vecino] = actual
                if dfs_recursivo(vecino):
                    return True
                    
        return False
    
    # Realizar búsqueda
    if dfs_recursivo(inicio):
        # Reconstruir el camino si se encontró
        camino = []
        actual = destino
        while actual is not None:
            camino.insert(0, actual)
            actual = predecesores.get(actual)
        return camino
    return None

def test_recorrido_profundidad():
    """
    Test para verificar el recorrido en profundidad usando datos de prueba.
    """
    try:
        # Crear datos de prueba
        usuarios_data = [
            "25143909I,Lucia,Lopez,1955-06-07",
            "76929765H,Juan,Rodriguez,1987-11-30",
            "18909774Z,Maria,Diaz,1995-01-05"
        ]

        relaciones_data = [
            "18909774Z,25143909I,31,170"
        ]

        # Crear la red social
        red = Red_social()

        # Diccionario para almacenar usuarios por DNI
        usuarios_por_dni = {}

        # Añadir usuarios
        for linea in usuarios_data:
            usuario = Usuario.parse(linea.strip())
            red.add_vertex(usuario)
            usuarios_por_dni[usuario.dni] = usuario

        # Añadir relaciones
        for linea in relaciones_data:
            dni1, dni2, interacciones, dias = linea.strip().split(',')
            usuario1 = usuarios_por_dni.get(dni1)
            usuario2 = usuarios_por_dni.get(dni2)
            
            if usuario1 and usuario2:
                relacion = Relacion.of(int(interacciones), int(dias))
                red.add_edge(usuario1, usuario2, relacion)
                red.add_edge(usuario2, usuario1, relacion)

        # Realizar búsqueda en profundidad
        inicio = usuarios_por_dni["25143909I"]  # Lucia
        destino = usuarios_por_dni["76929765H"]  # Juan
        
        camino = dfs_modificado(red, inicio, destino)
        
        # Mostrar resultados
        if camino:
            print(f"\nCamino encontrado desde {inicio.dni} hasta {destino.dni}:")
            print(camino)
            print(f"Longitud del camino: {len(camino) - 1} pasos")
        else:
            print(f"\nNo hay conexión directa entre {inicio.dni} y {destino.dni}.")
        
    except Exception as e:
        print(f"Error al realizar el recorrido DFS: {e}")
        import traceback
        traceback.print_exc()

def main():
    """
    Función principal para ejecutar los tests.
    """
    print("Iniciando test de recorrido en profundidad...")
    test_recorrido_profundidad()
    print("\nTest completado.")

if __name__ == "__main__":
    main()