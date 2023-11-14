# Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0. Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.

def monto():
    compra = int(input("Introduce una cantidad: "))
    total = 0
    while compra != 0:
        if compra == 0:
            break
        if compra > 0:
            total = total + compra
            if total > 1000:
                total = total * 1.10
            final = f"El total es de {total}"
        compra = int(input("Introduce una cantidad: "))
    print(final)

def main():
    monto()



if __name__ == "__main__":
    main()
