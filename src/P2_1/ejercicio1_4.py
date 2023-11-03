def pares(num):
    #retornará si el numero es par o impar
    resto = num % 2
    if resto == 0:
        return "El número es par."
    else:
        return "El número es impar."

def main():
    num = int(input("Introduce un número: "))
    print(pares(num))

if __name__ == "__main__":
    main()

