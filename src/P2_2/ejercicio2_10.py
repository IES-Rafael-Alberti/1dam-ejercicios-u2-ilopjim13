# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

def primos(num):
    cont = 2
    if num == 2:
        return "Es primo"
    while cont <= num - 1:
        div = num % 2
        cont += 1
        if div == 0:
            return "No es primo"
    if div != 0:
        return "Es primo"

def main():
    num = int(input("Introduce un numero: "))
    print(primos(num))

if __name__ == "__main__":
    main()

