def entrada(edad):
    if edad <= 0:
        return "Error"
    elif edad > 0 and edad < 4:
        return "La entrada es gratis"
    elif edad >= 4 and edad < 18:
        return "Debe pagar 5€ por la entrada."
    else:
        return "Debe pagar 10€ por la entrada."

def main():
    edad = int(input("Introduzca su edad: "))
    print(entrada(edad))

if __name__ == "__main__":
    main()
