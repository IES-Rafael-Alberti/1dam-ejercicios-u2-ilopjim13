# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

def edades(edad):
    for i in range(1,edad + 1):
        print(i,end=" ")

edad= int(input("Introduce tu edad: "))

def main():
    edades(edad)

if __name__ == "__main__":
    main()
