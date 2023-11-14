# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

def palabras(palabra):
    count = 1
    while count <= 10:
        count += 1
        print(palabra)

def main():
    palabra = input("Introduce una palabra: ")
    palabras(palabra)

if __name__ == "__main__":
    main()
