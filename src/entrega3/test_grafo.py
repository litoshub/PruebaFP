import os
from entrega3.red_social import Red_social
from entrega3.E_grafo import E_Grafo
from entrega3.grafo import Grafo
from entrega2.tipos.Cola import Cola
from entrega2.tipos.Pila import Pila
from entrega3.Recorrido import Recorrido
from entrega3.relacion import Relacion
from entrega3.Usuario import Usuario
def test_grafo():
    """
    Test para verificar la funcionalidad del grafo usando los datos de los archivos txt.
    """
    # Imprimir información de debug
    print("Directorio actual:", os.getcwd())
    print("Contenido del directorio:", os.listdir())

    # Crear datos de prueba en memoria
    #el archivo usuarios.txt no me lo encontraba por ningún metodo si no se hubiera hecho diferente
    usuarios_data = [
        "45718832U,Carlos,Lopez,1984-01-14",
        "71894470A,Carlos,Martinez,1990-05-20",
        "82007713N,Carlos,Garcia,1988-03-15",
        "16274768S,Juan,Perez,1995-07-22",
        "76929765H,Juan,Rodriguez,1987-11-30"
    ]

    relaciones_data = [
        "45718832U,71894470A,48,279",
        "45718832U,82007713N,35,180",
        "16274768S,76929765H,62,365"
    ]

    # Crear la red social
    red = Red_social()

    # Añadir usuarios
    for linea in usuarios_data:
        usuario = Usuario.parse(linea.strip())
        red.add_vertex(usuario)
        red._usuarios_dni[usuario.dni] = usuario

    # Añadir relaciones
    for linea in relaciones_data:
        dni1, dni2, interacciones, dias = linea.strip().split(',')
        usuario1 = red._usuarios_dni.get(dni1)
        usuario2 = red._usuarios_dni.get(dni2)
        
        if usuario1 and usuario2:
            relacion = Relacion.of(int(interacciones), int(dias))
            red.add_edge(usuario1, usuario2, relacion)

    # Mostrar resultados
    print("\n************** Nº Predecesores de cada vértice")
    for usuario in sorted(red.vertex_set(), key=lambda u: u.dni):
        predecesores = red.predecessors(usuario)
        print(f"{usuario.dni} - {usuario.nombre} -- {len(predecesores)}")
        
    print("\n************** Nº Vecinos de cada vértice")
    for usuario in sorted(red.vertex_set(), key=lambda u: u.dni):
        vecinos = red.successors(usuario)
        print(f"{usuario.dni} - {usuario.nombre} -- {len(vecinos)}")

def main():
    """
    Función principal para ejecutar los tests.
    """
    print("Iniciando tests del grafo...")
    test_grafo()
    print("\nTests completados.")

if __name__ == "__main__":
    main()
    