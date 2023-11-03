# Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el 0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene. Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.

def sumadigitospositivos(num):
    while True:
        if num == "0":
            break
        elif num < "0":
            print("Error.")
        elif num >= "0":
            break


def sonpares(num):
    if num == "0":
        return False
    else:
        return int(num) % 2 == 0

def digitospares(num):
    par = 0
    impar = 0
    while int(num) > 0:
        digito = int(num) % 10
        if sonpares(digito):
            par += 1
        else:
            impar += 1
        num = int(num) // 10
    print(f"Numeros pares: {par}")
    print(f"Numeros impares: {impar}")


def main():
    pares = 0
    impares = 0
    while True:
        num = input("Introduce un numero: ")
        sumadigitospositivos(num)
        if sonpares(num) == True:
            pares += 1
        else:
            if num == "0":
                exit
            else:
                impares += 1
        if int(num) == 0:
            print(f"Numeros totales de pares: {pares}")
            print(f"Numeros totales de impares: {impares}")
            break 
        else:
            digitospares(num)

if __name__ == "__main__":
    main()