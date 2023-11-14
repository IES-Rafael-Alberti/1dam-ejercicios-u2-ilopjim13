# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

# Formula para calcular El capital tras un año.
# amount *= 1 + interest / 100
# En donde:
# - amount: Cantidad a invertir
# - interest: Interes porcentual anual 


def inversion(amount, interest, tiempo):
    cont = 0
    num = 0
    while cont < tiempo:
        amount *= 1 + interest / 100
        num += 1
        print("Año {}: {:.2f}€".format(num,amount))
        cont += 1

def main():
    amount = int(input("Introduce la cantidad a invertir: "))
    interest = int(input("Introduce el interes anual: "))
    tiempo = int(input("Introduce los años: "))
    inversion(amount, interest, tiempo)

if __name__ == "__main__":
    main()