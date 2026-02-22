# 3) main.py

from modelos.producto import Producto
from servicios.inventario import Inventario


# -------- Funciones auxiliares para entrada segura --------

def leer_int(mensaje: str, minimo=None) -> int:   #Lee un entero desde consola y valida un mínimo opcional.
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"Debe ser >= {minimo}.")
                continue
            return valor
        except ValueError:
            print("Ingresa un número entero válido.")

def leer_float(mensaje: str, minimo=None) -> float:  #Lee un float desde consola y valida un mínimo opcional.
    while True:
        try:
            valor = float(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"Debe ser >= {minimo}.")
                continue
            return valor
        except ValueError:
            print("Ingresa un número decimal válido.")

def leer_texto(mensaje: str) -> str:   #Lee un texto no vacío desde consola.
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("El texto no puede estar vacío.")

# -------- Menú principal --------

def mostrar_menu() -> None:    #Muestra el menú de opciones en consola.
    print("\n" + "=" * 40)
    print("ALMACÉN APP - INVENTARIO")
    print("=" * 40)
    print("1) Añadir producto")
    print("2) Eliminar producto")
    print("3) Actualizar producto")
    print("4) Buscar producto por ID")
    print("5) Listar inventario")
    print("6) Salir")