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