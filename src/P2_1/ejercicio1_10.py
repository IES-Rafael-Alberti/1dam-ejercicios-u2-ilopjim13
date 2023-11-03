def pizzeria(pizza):
    if pizza == "vegetariana":
        print ("Estos son los ingredientes vegetarianos: Pimiento y tofu")
        ingrediente = input("Eliga un ingrediente para su pizza: ")
        if ingrediente == "pimiento":
            return f"Su pizza elegida es la vegetariana con {ingrediente} como ingrediente."
        elif ingrediente == "tofu":
            return f"Su pizza elegida es la vegetariana con {ingrediente} como ingrediente."
    elif pizza == "no vegetariana":
        print ("Estos son los ingredientes no vegetarianos: Peperoni, Jamón y Salmón")
        ingrediente = input("Eliga un ingrediente para su pizza: ")
        if ingrediente == "peperoni":
            return f"Su pizza elegida es la no vegetariana con {ingrediente} como ingrediente."
        elif ingrediente == "jamón":
            return f"Su pizza elegida es la no vegetariana con {ingrediente} como ingrediente."
        elif ingrediente == "salmón":
            return f"Su pizza elegida es la no vegetariana con {ingrediente} como ingrediente."

def main():
    pizza = input("Elige entre la pizza vegetariana o la no vegetariana: ")
    print(pizzeria(pizza))

if __name__ == "__main__":
    main()
