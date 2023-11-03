# Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.

def sumadigitos(num):
    num2 = ""
    num3 = 0
    for num2 in num:
        num2 = int(num2)
        num3 = num2 + num3
    return num3

def main():
    num = input("Introduce un numero: ")
    print(sumadigitos(num))

if __name__ == "__main__":
    main()
