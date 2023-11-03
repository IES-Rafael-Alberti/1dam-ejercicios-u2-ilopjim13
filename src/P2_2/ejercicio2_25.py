# Solicitar al usuario que ingrese una frase y luego informar cuál fue la palabra más larga (en caso de haber más de una, mostrar la primera) y cuántas palabras había. Precondición: se tomará como separador de palabras al carácter “ “ (espacio), ya sea uno o más.

def separador(frase):
    separada = frase.split(" ")
    mayor = ""
    for i in separada:
        if len(i) > len(mayor):
            mayor = i
    return f"La palabra mas larga es '{mayor}' de {len(separada)} palabras"

def main():
    frase = input("Introduce una frase: ")
    print(separador(frase))

if __name__ == "__main__":
    main()