'''
Created on 16 dic 2024

@author: carlo
'''
from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class Relacion:
    """
    Representa una relación entre dos usuarios en el sistema.
    """
    _id: int
    _interacciones: int
    _dias_activa: int
    
    # Contador estático para generar IDs únicos
    _xx_num: int = 0

    @property
    def id(self) -> int:
        """Devuelve el ID único de la relación."""
        return self._id

    @property
    def interacciones(self) -> int:
        """Devuelve el número de interacciones de la relación."""
        return self._interacciones

    @property
    def dias_activa(self) -> int:
        """Devuelve el número de días activos de la relación."""
        return self._dias_activa

    @staticmethod
    def of(interacciones: int, dias_activa: int) -> Relacion:
        """
        Crea una nueva instancia de Relacion.
        
        :param interacciones: Número de interacciones entre usuarios
        :param dias_activa: Número de días que la relación ha estado activa
        :return: Nueva instancia de Relacion
        :raises ValueError: Si los valores son negativos
        """
        # Validar valores positivos
        if interacciones < 0 or dias_activa < 0:
            raise ValueError("Las interacciones y días activos deben ser positivos")

        # Incrementar el contador y asignar ID
        Relacion._xx_num += 1
        nuevo_id = Relacion._xx_num

        return Relacion(nuevo_id, interacciones, dias_activa)

    def __str__(self) -> str:
        """
        Devuelve la representación en cadena de la relación.
        """
        return f"({self._id} - días activa: {self._dias_activa} - num interacciones {self._interacciones})"