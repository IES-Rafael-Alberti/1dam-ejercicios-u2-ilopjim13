# Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, finalizando cuando se reciba un cero. Imprimir la cantidad de números primos ingresados.
from ejercicio2_10 import primos

def primosingresados(num):
    while num != 0:
        if num == 0:
            break
        elif num < 0:
            print("Error.")
        elif num > 0:
            break

def main():
    cuenta = 0
    while True:
        num = int(input("Introduce un numero: "))
        primosingresados(num)
        if num == 0:
            break
        if primos(num) == "Es primo":
                cuenta += 1
    print(f"Se han ingresado un total de {cuenta} primos")

if __name__ == "__main__":
    main()

