def pizzas(pizza):
    if pizza == 1:
        print ("Estos son los ingredientes vegetarianos:")
        print ("- Pimiento")
        print ("- Tofu")
        return "Estos son los ingredientes vegetarianos: Pimiento y Tofu."
    elif pizza == 2:
        print ("Estos son los ingredientes no vegetarianos: ")
        print ("- Peperoni ")
        print ("- Jamón")
        print ("- Salmón")
        return "Estos son los ingredientes no vegetarianos: Peperoni, Jamón y Salmón."
    else:
        print("Error.")
        return "Error."


def ingredientesveganos(ingrediente):
    if ingrediente == 1:
        print("Su pizza elegida es la vegetariana con pimiento como ingrediente.")
        return "Su pizza elegida es la vegetariana con pimiento como ingrediente."
    elif ingrediente == 2:
        print("Su pizza elegida es la vegetariana con tofu como ingrediente.")
        return "Su pizza elegida es la vegetariana con tofu como ingrediente."
    else:
        print("Error.")
        return"Error."


def ingredientesnoveganos(ingrediente):
    if ingrediente == 1:
        print("Su pizza elegida es la no vegetariana con peperoni como ingrediente.")
        return "Su pizza elegida es la no vegetariana con peperoni como ingrediente."
    elif ingrediente == 2:
        print("Su pizza elegida es la no vegetariana con jamón como ingrediente.")
        return "Su pizza elegida es la no vegetariana con jamón como ingrediente."
    elif ingrediente == 3:
        print("Su pizza elegida es la no vegetariana con salmón como ingrediente.")
        return "Su pizza elegida es la no vegetariana con salmón como ingrediente."
    else:
        print("Error.")
        return"Error."


def pizzeria(pizza):
    pizzas(pizza)
    if pizza == 1:
        ingrediente = int(input("Eliga un ingrediente para su pizza: Pimiento (1) o Tofu (2): "))
        ingredientesveganos(ingrediente)
        return ingrediente
    if pizza == 2:
        ingrediente = int(input("Eliga un ingrediente para su pizza: Peperoni (1), Jamón (2) o Salmón(3) : "))
        ingredientesnoveganos(ingrediente)
        return ingrediente


def main():
    pizza = int(input("Elige entre la pizza vegetariana (1) o la no vegetariana (2): "))
    pizzeria(pizza)


if __name__ == "__main__":
    main()
