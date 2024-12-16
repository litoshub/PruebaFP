'''
Created on 16 dic 2024

@author: carlo
'''
from __future__ import annotations
from dataclasses import dataclass
from datetime import date, datetime
import re

@dataclass(frozen=True)
class Usuario:
    """
    Representa un usuario en el sistema.
    """
    _dni: str
    _nombre: str
    _apellidos: str
    _fecha_nacimiento: date

    @property
    def dni(self) -> str:
        """Devuelve el DNI del usuario."""
        return self._dni

    @property
    def nombre(self) -> str:
        """Devuelve el nombre del usuario."""
        return self._nombre

    @property
    def apellidos(self) -> str:
        """Devuelve los apellidos del usuario."""
        return self._apellidos

    @property
    def fecha_nacimiento(self) -> date:
        """Devuelve la fecha de nacimiento del usuario."""
        return self._fecha_nacimiento

    @staticmethod
    def of(dni: str, nombre: str, apellidos: str, fecha_nacimiento: date) -> Usuario:
        """
        Crea una nueva instancia de Usuario.
        
        :param dni: DNI del usuario (8 dígitos + letra)
        :param nombre: Nombre del usuario
        :param apellidos: Apellidos del usuario
        :param fecha_nacimiento: Fecha de nacimiento del usuario
        :return: Nueva instancia de Usuario
        :raises ValueError: Si los datos no son válidos
        """
        # Validar DNI
        if not re.match(r'^\d{8}[A-Z]$', dni):
            raise ValueError("DNI inválido: debe tener 8 dígitos seguidos de una letra mayúscula")

        # Validar fecha de nacimiento
        if fecha_nacimiento >= date.today():
            raise ValueError("Fecha de nacimiento debe ser anterior a la fecha actual")

        # Validar nombre y apellidos
        if not nombre or not apellidos:
            raise ValueError("Nombre y apellidos no pueden estar vacíos")

        return Usuario(dni, nombre, apellidos, fecha_nacimiento)

    @staticmethod
    def parse(texto: str) -> Usuario:
        """
        Crea una instancia de Usuario a partir de una cadena de texto.
        
        :param texto: Cadena con formato "DNI,nombre,apellidos,fecha_nacimiento"
        :return: Nueva instancia de Usuario
        :raises ValueError: Si el formato del texto no es válido
        """
        try:
            dni, nombre, apellidos, fecha = texto.strip().split(',')
            fecha_nacimiento = datetime.strptime(fecha, '%Y-%m-%d').date()
            return Usuario.of(dni, nombre, apellidos, fecha_nacimiento)
        except ValueError as e:
            raise ValueError(f"Formato de texto inválido: {e}")

    def __str__(self) -> str:
        """
        Devuelve la representación en cadena del usuario (dni - nombre).
        """
        return f"{self._dni} - {self._nombre}"