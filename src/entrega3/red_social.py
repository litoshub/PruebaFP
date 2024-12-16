'''
Created on 16 dic 2024

@author: carlo
'''
from __future__ import annotations
from typing import Dict, Optional, Set
from entrega3.E_grafo import E_Grafo
from entrega3.grafo import Grafo
from entrega2.tipos.Cola import Cola
from entrega2.tipos.Pila import Pila
from entrega3.Recorrido import Recorrido
from entrega3.relacion import Relacion
from entrega3.Usuario import Usuario
class Red_social(E_Grafo[Usuario, Relacion]):
    """
    Representa una red social como un grafo donde los nodos son usuarios
    y las aristas son relaciones entre ellos.
    """
    def __init__(self, es_dirigido: bool = False):
        """
        Inicializa una nueva red social.
        
        :param es_dirigido: Indica si el grafo es dirigido
        """
        super().__init__(es_dirigido)
        self._usuarios_dni: Dict[str, Usuario] = {}

    @staticmethod
    def of(es_dirigido: bool = False, tipo_recorrido: bool = False) -> Red_social:
        """
        Crea una nueva instancia de Red_social.
        
        :param es_dirigido: Indica si el grafo es dirigido
        :param tipo_recorrido: Indica el tipo de recorrido (False para BACK)
        :return: Nueva instancia de Red_social
        """
        return Red_social(es_dirigido)

    @staticmethod
    def parse(archivo_usuarios: str, archivo_relaciones: str) -> Red_social:
        """
        Crea una Red_social a partir de archivos de usuarios y relaciones.
        
        :param archivo_usuarios: Ruta al archivo de usuarios
        :param archivo_relaciones: Ruta al archivo de relaciones
        :return: Nueva instancia de Red_social con los datos cargados
        """
        red = Red_social()

        # Cargar usuarios
        with open(archivo_usuarios, 'r', encoding='utf-8') as f:
            for linea in f:
                if linea.strip():
                    usuario = Usuario.parse(linea.strip())
                    red.add_vertex(usuario)
                    red._usuarios_dni[usuario.dni] = usuario

        # Cargar relaciones
        with open(archivo_relaciones, 'r', encoding='utf-8') as f:
            for linea in f:
                if linea.strip():
                    dni1, dni2, interacciones, dias = linea.strip().split(',')
                    usuario1 = red._usuarios_dni.get(dni1)
                    usuario2 = red._usuarios_dni.get(dni2)
                    
                    if usuario1 and usuario2:
                        relacion = Relacion.of(int(interacciones), int(dias))
                        red.add_edge(usuario1, usuario2, relacion)

        return red

    def __str__(self) -> str:
        """
        Devuelve una representación en cadena de la red social.
        """
        resultado = []
        for usuario in self.vertex_set():
            relaciones = []
            for vecino in self.successors(usuario):
                relacion = self.edge_weight(usuario, vecino)
                if relacion:
                    relaciones.append(f"{vecino}: {relacion}")
            resultado.append(f"{usuario} -> {', '.join(relaciones)}")
        return "\n".join(resultado)