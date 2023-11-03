# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

def tabla():
    num = 1
    tabla = f"{num} x 10 = "
    while num <= 10:
        mult = num * 10
        tabla = f"{num} x 10 = {mult}"
        num += 1
        print(tabla)

def main():
    tabla()

if __name__ == "__main__":
    main()