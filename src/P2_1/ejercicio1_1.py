# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

def mayoredad(n1):
    #Si la edad es mayor o igual a 18 retornará que es mayor de edad y si no es asi retornará que es menor de edad
    if n1 <= 0:
        return "Error."
    if n1 >= 18:
        return "Eres mayor de edad."
    else:
        return "Eres menor de edad."
    
def main():
    n1 = int(input("Introduce tu edad: "))
    print(mayoredad(n1))

if __name__ == "__main__":
    main()



