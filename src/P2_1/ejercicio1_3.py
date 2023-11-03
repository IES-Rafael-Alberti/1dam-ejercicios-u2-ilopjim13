def division(num1, num2):
    #Realizara una división entre dos números y dara error si se divide entre 0
    if num1 == 0 or num2 == 0:
        return "Error no se puede dividir entre 0"
    else:
        return num1 / num2

def main():
    num1 = int(input("Introduce un número: "))
    num2 = int(input("Introduce otro número: "))
    print(division(num1, num2))

if __name__ == "__main__":
    main()


