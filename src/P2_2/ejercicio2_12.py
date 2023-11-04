# Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

def letra(palabra, letras):
    cont = 0
    for i in palabra:
        if letras == i:
            cont += 1
    print(f"Esta letra aparece un total de {cont} veces.")
    return cont

def main():
    palabra = input("Introduce una palabra: ")
    letras = input("Introduce una letra: ")
    letra(palabra, letras)

if __name__ == "__main__":
    main()