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
    
    def asegurar_archivo(self) -> None:                #Garantiza que carpeta y archivo existan.
        carpeta = os.path.dirname(self.ruta_archivo)

        if not os.path.exists(carpeta):          #Si la carpeta no existe, se crea automáticamente. Esto evita errores al intentar escribir en un archivo dentro de una carpeta inexistente.
            os.makedirs(carpeta, exist_ok=True)

        if not os.path.exists(self.ruta_archivo):
            with open(self.ruta_archivo, "w", encoding="utf-8"):
                pass

    def _producto_a_linea(self, producto: Producto) -> str:   #Convierte un Producto a una línea TXT.
        return producto.to_linea()
    
    def _linea_a_producto(self, linea: str) -> Optional[Producto]: #Convierte una línea del archivo a un objeto Producto. Si la línea es corrupta, devuelve None.
        try:
            return Producto.from_linea(linea)
        except Exception:
            return None 

    # -------- Persistencia --------
    def cargar_desde_archivo(self) -> None:  #Reconstruye la lista desde el archivo.
        try:
            self.asegurar_archivo()
            self.__productos.clear()

            with open(self.ruta_archivo, "r", encoding="utf-8") as f:  #Se lee el archivo línea por línea para reconstruir los objetos Producto. Si el archivo no existe, se crea automáticamente. Si el archivo está vacío, simplemente no se agregan productos a la lista.
                for linea in f:
                    linea = linea.strip()
                    if not linea:
                        continue

                    producto = self._linea_a_producto(linea)   #Si la línea es válida, se agrega el producto a la lista. Si la línea está corrupta, se ignora y se continúa con la siguiente línea.
                    if producto:
                        idx = self._buscar_indice_por_id(producto.get_id())
                        if idx != -1:
                            self.__productos[idx] = producto
                        else:
                            self.__productos.append(producto)

            print("Inventario cargado correctamente.")

        except PermissionError:                              #Si no se tienen permisos para leer el archivo, se muestra un mensaje de error específico.
            print("Sin permisos para leer el archivo.")
        except Exception as e:
            print(f"Error al cargar archivo: {e}") 

    def guardar_en_archivo(self) -> bool:      #Sobrescribe el archivo con el estado actual. Devuelve True si se guardó correctamente, False si hubo un error.
        try:
            self.asegurar_archivo()

            with open(self.ruta_archivo, "w", encoding="utf-8") as f:
                for p in self.__productos:
                    f.write(self._producto_a_linea(p) + "\n")

            return True

        except PermissionError:
            print("Sin permisos para escribir en el archivo.")
            return False
        except Exception as e:
            print(f"Error al guardar archivo: {e}")
            return False
        
    # -------- Métodos de gestión de productos (CRUD) (Create, Read, Update, Delate)--------
    def agregar_producto(self, producto: Producto) -> bool:      #Agrega un producto si el ID no existe y guarda en archivo. 
        if self._buscar_indice_por_id(producto.get_id()) != -1:  
            print("El ID ya existe.")
            return False

        self.__productos.append(producto)  
        self.guardar_en_archivo()
        print("Producto agregado.")
        return True

    def eliminar_producto(self, producto_id: int) -> bool:  #Elimina por ID y guarda cambios en archivo.
        indice = self._buscar_indice_por_id(producto_id)
        if indice == -1:
            print("No existe producto con ese ID.")
            return False

        self.__productos.pop(indice)
        self.guardar_en_archivo()
        print("Producto eliminado.")
        return True

    def actualizar_producto(self, producto_id: int, nueva_cantidad=None, nuevo_precio=None) -> bool:  #Actualiza cantidad y/o precio por ID y guarda en archivo.
        indice = self._buscar_indice_por_id(producto_id)
        if indice == -1:
            print("No existe producto con ese ID.")
            return False

        producto = self.__productos[indice]

        if nueva_cantidad is not None:
            producto.set_cantidad(nueva_cantidad)

        if nuevo_precio is not None:
            producto.set_precio(nuevo_precio)

        self.guardar_en_archivo()
        print("Producto actualizado.")
        return True                

    def buscar_por_id(self, producto_id: int) -> Optional[Producto]: #Retorna el producto por ID o None si no existe.
        indice = self._buscar_indice_por_id(producto_id)
        return None if indice == -1 else self.__productos[indice]