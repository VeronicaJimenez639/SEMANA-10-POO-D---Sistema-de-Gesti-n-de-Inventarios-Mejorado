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

def main() -> None:             #Punto de entrada: bucle principal del menú y llamadas al servicio Inventario.
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = leer_int("Elige opción: ", minimo=1)

        if opcion == 1:
            try:
                producto = Producto(
                    leer_int("ID: ", minimo=1),
                    leer_texto("Nombre: "),
                    leer_int("Cantidad: ", minimo=0),
                    leer_float("Precio: ", minimo=0.0)
                )
                inventario.agregar_producto(producto)
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == 2:
            inventario.eliminar_producto(leer_int("ID: ", minimo=1))

        elif opcion == 3:
            producto_id = leer_int("ID: ", minimo=1)
            nueva_cantidad = leer_int("Nueva cantidad: ", minimo=0)
            nuevo_precio = leer_float("Nuevo precio: ", minimo=0.0)
            inventario.actualizar_producto(producto_id, nueva_cantidad, nuevo_precio)

        elif opcion == 4:
            producto = inventario.buscar_por_id(leer_int("ID: ", minimo=1))
            print(producto if producto else "No encontrado.")

        elif opcion == 5:
            productos = inventario.listar_productos()
            if not productos:
                print("Inventario vacío.")
            else:
                for p in productos:
                    print(p)

        elif opcion == 6:
            print("Saliendo...")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":  
    main() 