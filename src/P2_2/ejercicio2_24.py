# Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, finalizando cuando se reciba un cero. Imprimir la cantidad de números primos ingresados.
from src.P2_2.ejercicio2_10 import primos #Para pytest
#from ejercicio2_10 import primos #Para ejecutar el codigo

def primosingresados(num, cuenta):
    while True:
        if num == 0:
            break
        if num < 0:
            return("Error.")
        if primos(num) == "Es primo":
            cuenta += 1
            break
        else:
            break
    return cuenta


def pedirnum():
    num = int(input("Introduce un numero: "))
    return num

def main():
    cuenta = 0
    while True:
        num = pedirnum()
        cuenta = primosingresados(num,cuenta)
        if num == 0:
            break
    print(primosingresados(num, cuenta))

if __name__ == "__main__":
    main()

