# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

def deletrear(palabra):
    for letra in reversed(palabra):
        print(letra)
        

def main():
    palabra = input("Introduce una palabra: ")
    deletrear(palabra)

if __name__ == "__main__":
    main()
