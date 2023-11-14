# Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.

def sumatoriaMayor(num):
    num2 = 0
    while num != 0:
        num = int(input())
        if num < 0:
            print("Error.")
        elif num == 0:
            break
        elif  num > num2:
            num2= num
    return num2

def main():
    num = int(input())
    print(sumatoriaMayor(num))

if __name__ == "__main__":
    main()