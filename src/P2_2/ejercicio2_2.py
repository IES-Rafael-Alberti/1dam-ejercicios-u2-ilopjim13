# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

def edades(edad):
    if edad <= 0:
        print("Error.")
    for i in range(1,edad + 1):
        if i < edad:
            print(i,end=" ")
        if i == edad:
            print(i)


def main():
    edad= int(input("Introduce tu edad: "))
    edades(edad)

if __name__ == "__main__":
    main()
