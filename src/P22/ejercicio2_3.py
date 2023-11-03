# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

def impares(num):
    for i in range(1,num + 1, 2):
        if i < num - 1:
            print(i,end=", ")
        elif i >= num or i== num - 1:
            print(i,end="")

num = int(input("Introduce un numero positivo: "))

def main():
    impares(num)

if __name__ == "__main__":
    main()
