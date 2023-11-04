# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

def deletrear(palabra):
    for i in reversed(palabra):
        print(i)
    return ''.join(reversed(palabra))#para el pytest

def main():
    palabra = input("Introduce una palabra: ")
    deletrear(palabra)

if __name__ == "__main__":
    main()
