# Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.

def sumatoria(num):
    suma = num
    while num != 0:
        num = int(input())
        if num == 0:
            break
        else:
            suma = suma + num
    return suma

def main():
    num = int(input())
    print(sumatoria(num))

if __name__ == "__main__":
    main()