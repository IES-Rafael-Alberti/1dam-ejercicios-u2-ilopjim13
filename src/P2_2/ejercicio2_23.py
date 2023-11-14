# Crear un programa que permita al usuario ingresar títulos de libros por teclado, finalizando el ingreso al leerse el string “*” (asterisco). Cada vez que el usuario ingrese un string de longitud 1 que contenga sólo una barra (“/”) se considera que termina una línea. Por cada línea completa, informar cuántos dígitos numéricos (del 0 al 9) aparecieron en total (en todos los títulos de libros que componen en esa línea). Finalmente, informar cuántas líneas completas se ingresaron.

# Ejemplo de ejecución:
# Libro: Los 3 mosqueteros
# Libro: Historia de 2 ciudades
# Libro: /
# Línea completa. Aparecen 2 dígitos numéricos.
# Libro: 20000 leguas de viaje submarino
# Libro: El señor de los anillos
# Libro: /
# Línea completa. Aparecen 5 dígitos numéricos.
# Libro: 20 años después
# Libro: *
# Fin. Se leyeron 2 líneas completas.


def titulos(libro):
    lineas = 0
    total = 0
    while libro != "*":
        if libro == "*":
            break
        for digito in libro:
            if digito.isdigit():
                total += 1
        if libro == "/":
            lineas += 1
            print(f"Línea completa. Aparecen {total} dígitos numéricos.")
            total = 0
        libro = input("Libro: ")
    print(f"Fin. Se leyeron {lineas} líneas completas.")

def main():
    libro = input("Libro: ")
    titulos(libro)

if __name__ == "__main__":
    main()