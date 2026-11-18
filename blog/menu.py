# blog/menu.py
# Menú e interacción con el usuario (todo el manejo de input() está acá)


def mostrar_menu():
    """Muestra el menú y retorna la opción elegida como número (o None si no es un número)."""
    print("\n--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Validar posts")
    print("5. Salir")

    # try-except: si el usuario escribe texto, int() falla y el programa no se cierra
    try:
        return int(input("Elegí una opción: "))
    except ValueError:
        print("Error: tenés que ingresar un número del 1 al 5.")
        return None


def pedir_texto(mensaje):
    """Pide un texto por consola y lo retorna sin espacios al principio ni al final."""
    return input(mensaje).strip()
