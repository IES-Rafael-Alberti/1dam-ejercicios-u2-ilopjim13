# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
# 
# 1
# 3 1
# 5 3 1
# 7 5 3 1
# 9 7 5 3 1

def triangulo(num):
    cont = 1
    suma = 1
    serie = ""
    while cont <= num:
        cont += 1
        serie = f"{str(suma)} {serie}"
        suma = suma + 2
        print(serie)

num = int(input("Introduce un numero: "))

def main():
    triangulo(num)

if __name__ == "__main__":
    main()
