# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

def numeros(num):
    for i in range(num , -1, -1):
        if i >= 1:
            print(i,end=", ")
        elif i >= 0:
            print(i,end="")

num = int(input("Introduce un numero positivo: "))

def main():
    numeros(num)

if __name__ == "__main__":
    main()
