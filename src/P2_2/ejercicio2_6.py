# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
#
# *
# **
# ***
# ****
# *****

def triangulo(num):
    cont = 1
    serie = ""
    if num <= 0:
        print("Error.")
        return "Error."
    while cont <= num:
        cont += 1
        serie = serie + "*"
        print(serie)
    return serie


def main():
    num = int(input("Introduce un numero: "))
    triangulo(num)

if __name__ == "__main__":
    main()
