# Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.

def sumatoriaMayor(num):
    while num != 0:
        num2 = num
        num = int(input())
        if num < 0:
            print("Error.")
        elif num == 0:
            break
        elif num2 > num:
            print(num2)

def main():
    num = int(input())
    sumatoriaMayor(num)

if __name__ == "__main__":
    main()