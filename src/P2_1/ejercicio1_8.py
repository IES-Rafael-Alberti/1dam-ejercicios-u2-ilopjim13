def puntuacion(puntos):
    if puntos == 0.0 or puntos == 0.4 or puntos >= 0.6:
        if puntos == 0.0:
            return "El nivel de rendimiento es inaceptable por lo que la cantidad recibida será de 0 euros."
        elif puntos == 0.4:
            cantidad = 2400 * puntos
            return "El nivel es aceptable por lo que la cantidad recibida será de {:.0f}€.".format(cantidad)
        else:
            cantidad = 2400 * puntos
            return "El nivel es meritorio por lo que la cantidad recibida será de {:.0f}€.".format(cantidad)
    else:
        return "Puntuación errónea"

def main():
    puntos = float(input("Introduce la puntuación del empleado: "))
    print(puntuacion(puntos))

if __name__ == "__main__":
    main()

