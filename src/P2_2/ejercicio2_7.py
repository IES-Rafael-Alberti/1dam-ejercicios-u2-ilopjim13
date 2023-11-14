# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

def tabla():
    num = 1
    multi = 0
    tabla = f"{num} x {multi} = "
    while multi < 10:
        num = 1
        multi += 1
        print('')
        while num <= 10:
            mult = num * multi
            tabla = f"{num} x {multi} = {mult}"
            num += 1
            print(tabla)

def main():
    tabla()

if __name__ == "__main__":
    main()