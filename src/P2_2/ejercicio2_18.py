# Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.

def sumadigitospositivos(num):
    num2 = ""
    num3 = 0
    while True:
        if num == "-1":
            break
        elif int(num) < -1:
            return "Error."
        elif num >= "0":
            for num2 in num:
                num2 = int(num2)
                num3 = num2 + num3
        print(f"{num} = {num3}")
        
        break
    return num3


def sonpares(num):
    if num == "0":
        return False
    else:
        return int(num) % 2 == 0


def main():
    pares = 0
    while True:
        num = input("Introduce un numero: ")
        sumadigitospositivos(num)
        if sonpares(num):
            pares += 1
        if num == "-1":
            print(pares)
            break

if __name__ == "__main__":
    main()
