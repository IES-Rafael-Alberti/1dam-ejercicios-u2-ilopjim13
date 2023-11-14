def tributar(edad, ingreso):
    #Si es mayor de 16 y gana más de 1000 euros podrá tributar y sino no podrá
    if edad < 0 or ingreso < 0:
        return "Error."
    elif edad >= 16 and ingreso >= 1000:
        return "Puedes tributar."
    else:
        return "No puedes tributar."

def main():
    edad = int(input("Ingrese su edad: "))
    ingreso = int(input("Ingrese sus ingresos mensuales: "))
    print(tributar(edad, ingreso))

if __name__ == "__main__":
    main()