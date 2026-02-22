# 2) servicios/inventario.py

import os
from typing import Optional
from modelos.producto import Producto


class Inventario:
    """
    Gestiona el conjunto de productos.
    Responsabilidades:
    - Mantener la lista en memoria.
    - Sincronizar los cambios con un archivo TXT.
    - Manejar errores de lectura/escritura.
    """

    def __init__(self, ruta_archivo: str = None):
        # Lista principal en memoria
        self.__productos: list[Producto] = []