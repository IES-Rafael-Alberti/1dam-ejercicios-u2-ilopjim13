# Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3-finalizar programa. A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). Si elige una opción incorrecta, informarle del error. El menú se debe volver a mostrar luego de ejecutada cada opción, permitiendo volver a elegir. Si elige las opciones 1 ó 2 se imprimirá un texto. Si elige la opción 3, se interrumpirá la impresión del menú y el programa finalizará.


def opciones(opcion):

    match opcion:
        case "1":
            comenzar()
        case "2":
            limpiar()
        case "3":
            finalizar()



def comenzar():
    print("Comienza el programa")


def limpiar():
    print("Limpiando el listado")


def finalizar():
    exit


def main():
    while True:
        opcion = input("1- comenzar programa, 2- imprimir listado, 3-finalizar programa: ")
        if opcion == "1" or opcion == "2" or opcion == "3":
            opciones(opcion)
            if opcion == "3":
                break
        else:
            print("Error.")
            break


if __name__ == "__main__":
    main()