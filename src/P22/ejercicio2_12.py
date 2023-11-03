# Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

def letra(palabra, letras):
    if letras in palabra:
        print(letra)

def main():
    palabra = input("Introduce una palabra: ")
    letras = input("Introduce una letra: ")
    letra(palabra, letras)

if __name__ == "__main__":
    main()