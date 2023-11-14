# Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

def eco(palabra):
    while palabra != "salir":
        palabra = input("")
        if palabra == "salir":
            break
        else:
            print(palabra)

def main():
    palabra = input()
    print(palabra)
    eco(palabra)

if __name__ == "__main__":
    main()