# main.py
# Archivo principal: importa las piezas del paquete blog y coordina el flujo del menú.

from blog.datos import posts
from blog.menu import mostrar_menu, pedir_texto
from blog.operaciones import listar_posts, buscar_por_titulo, filtrar_por_tag, mostrar_resultados
from blog.validaciones import validar_post


def mostrar_validacion(lista):
    """Usa validar_post() en cada post y muestra cuáles son válidos y cuáles tienen errores."""
    print("\nResultado de la validación:")
    for posicion, post in enumerate(lista, start=1):
        es_valido, mensaje = validar_post(post)
        # Si el post no es un diccionario o no tiene id, se usa su posición en la lista
        identificador = post.get("id", posicion) if isinstance(post, dict) else posicion
        if es_valido:
            print(f"Post {identificador}: válido")
        else:
            print(f"Post {identificador}: error - {mensaje}")


def ejecutar():
    """Mantiene el menú activo y llama a la función que corresponde a cada opción."""
    while True:
        opcion = mostrar_menu()

        # Si la entrada no era un número, se vuelve a mostrar el menú
        if opcion is None:
            continue

        if opcion == 1:
            listar_posts(posts)

        elif opcion == 2:
            termino = pedir_texto("Buscar por titulo: ")
            if termino == "":
                print("La búsqueda no puede estar vacía.")
            else:
                resultados = buscar_por_titulo(posts, termino)
                mostrar_resultados(resultados, f"No se encontraron posts con '{termino}' en el título.")

        elif opcion == 3:
            tag = pedir_texto("Ingresá un tag: ")
            if tag == "":
                print("El tag no puede estar vacío.")
            else:
                resultados = filtrar_por_tag(posts, tag)
                mostrar_resultados(resultados, f"No hay posts con el tag '{tag}'.")

        elif opcion == 4:
            mostrar_validacion(posts)

        elif opcion == 5:
            print("Gracias por usar el sistema del blog. ¡Hasta luego!")
            break

        # Número fuera del rango del menú
        else:
            print("Opción inválida, intenta de nuevo")


# La ejecución solo arranca si se corre este archivo directamente
if __name__ == "__main__":
    ejecutar()
