# Este programa implementa un Sistema de Gestión de Inventario
# para un almacén. Permite registrar, actualizar,
# eliminar y consultar productos mediante un menú en consola.
#
# En la versión inicial (Semana 9), el inventario funcionaba
# únicamente en memoria utilizando listas. Esto significaba que
# al cerrar el programa, toda la información se perdía.
#
# En esta versión mejorada (Semana 10), se añadió:
# - Persistencia en archivo TXT para conservar los datos.
# - Carga automática del inventario al iniciar el sistema.
# - Manejo de excepciones para controlar errores de lectura
#   y escritura de archivos.
# - Creación automática de carpeta y archivo si no existen.
#
# Con estas mejoras, el sistema es más robusto, mantenible y
# cercano a una aplicación real.


# 1) modelos/producto.py

class Producto:
    """
    Representa un producto del inventario.
    Se encarga de:
    - Validar los datos (ID, nombre, cantidad, precio).
    - Convertirse a texto para guardarse en archivo.
    - Reconstruirse desde una línea del archivo.
    """

    SEPARADOR = "|"  # Formato en TXT: id|nombre|cantidad|precio

    def __init__(self, producto_id: int, nombre: str, cantidad: int, precio: float):
        # Se usan setters para asegurar validación desde la creación del objeto
        self.set_id(producto_id)
        self.set_nombre(nombre)
        self.set_cantidad(cantidad)
        self.set_precio(precio)

    # -------- Getters (lectura controlada de atributos privados) --------
    def get_id(self) -> int:
        return self.__id      #Retorna el identificador único del producto.

    def get_nombre(self) -> str:
        return self.__nombre    #Retorna el nombre del producto.

    def get_cantidad(self) -> int:
        return self.__cantidad   #Retorna la cantidad disponible.
    
    def get_precio(self) -> float:
        return self.__precio     #Retorna el precio unitario del producto.