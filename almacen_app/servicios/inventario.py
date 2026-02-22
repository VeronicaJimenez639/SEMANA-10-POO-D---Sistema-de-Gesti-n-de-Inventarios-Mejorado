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

        # Construcción de ruta relativa al archivo actual
        # Se usa ruta relativa al archivo para evitar problemas
        # si el programa se ejecuta desde otra carpeta o terminal diferente
        base_dir = os.path.dirname(__file__)
        if ruta_archivo is None:
            ruta_archivo = os.path.join(base_dir, "registros", "inventario.txt")

        self.ruta_archivo = ruta_archivo

        # Al iniciar el sistema, se carga el archivo automáticamente
        self.cargar_desde_archivo()

    # -------- Métodos internos --------
    def _buscar_indice_por_id(self, producto_id: int) -> int:    #Devuelve el índice del producto o -1 si no existe.
        for i, producto in enumerate(self.__productos):
            if producto.get_id() == producto_id:
                return i
        return -1