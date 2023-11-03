# Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase). Recorrer la frase, carácter a carácter, comparando con la letra buscada. Si el carácter no coincide, indicar que no hay coincidencia en esa posición (imprimiendo la posición) y continuar. Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución.

def coincide(letra, palabra):
    i = ""
    cont = 0
    coincide = letra in palabra
    if coincide == True:
        while i != letra:
            for i in palabra:
                cont += 1
                if i == letra:
                    break
        print(f"Coincide, la posicion es de esta letra es la {cont}")
    else:
        print(f"No existe coincidencias en esta posicion '{palabra}'")


def main():
    palabra = input("Introduce una palabra: ")
    letra = input("Introduce una letra: ")
    coincide(letra, palabra)

if __name__ == "__main__":
    main()
