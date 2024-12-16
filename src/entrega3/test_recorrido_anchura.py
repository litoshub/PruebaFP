from entrega3.red_social import Red_social
from entrega3.Usuario import Usuario
from entrega3.relacion import Relacion
from entrega2.tipos.Cola import Cola
from typing import List

def bfs_modificado(grafo: Red_social, inicio: 'Usuario', destino: 'Usuario') -> List['Usuario']:
    """
    Realiza un recorrido en anchura (BFS) desde un vértice inicial hasta un vértice destino.
    """
    visitados = set()
    predecesores = {inicio: None}
    cola = Cola.of()
    
    cola.add(inicio)
    
    while not cola.is_empty:  # Quitar los paréntesis porque es una propiedad
        vertice = cola.remove()
        
        if vertice == destino:
            break
            
        if vertice not in visitados:
            visitados.add(vertice)
            
            for vecino in grafo.successors(vertice):
                if vecino not in visitados and vecino not in predecesores:
                    cola.add(vecino)
                    predecesores[vecino] = vertice
    
    # Reconstruir el camino
    camino = []
    actual = destino
    
    while actual is not None:
        camino.insert(0, actual)
        actual = predecesores.get(actual)
        
    return camino

def test_recorrido_anchura():
    """
    Test para verificar el recorrido en anchura usando datos de prueba.
    """
    try:
        # Crear datos de prueba
        usuarios_data = [
            "25143909I,Lucia,Lopez,1955-06-07",
            "87345530M,Ana,Rodriguez,1964-03-02",
            "18909774Z,Maria,Diaz,1995-01-05"
        ]

        relaciones_data = [
            "87345530M,18909774Z,45,220",
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

        # Realizar búsqueda en anchura
        inicio = usuarios_por_dni["25143909I"]
        destino = usuarios_por_dni["87345530M"]
        
        camino = bfs_modificado(red, inicio, destino)
        
        # Mostrar resultados
        print("\nEl camino más corto desde", inicio.dni, "hasta", destino.dni, "es:")
        print(camino)
        print("La distancia mínima es:", len(camino) - 1, "pasos.")
        
    except Exception as e:
        print(f"Error al realizar el recorrido BFS: {e}")
        import traceback
        traceback.print_exc()

def main():
    """
    Función principal para ejecutar los tests.
    """
    print("Iniciando test de recorrido en anchura...")
    test_recorrido_anchura()
    print("\nTest completado.")

if __name__ == "__main__":
    main()
    