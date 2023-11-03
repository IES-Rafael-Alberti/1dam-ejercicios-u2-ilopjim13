def impositivo(renta):
    if renta <= 0:
        return "Error"
    elif renta > 0 and renta < 10000:
        return "Le corresponde un impositivo del 5%"
    elif renta >= 10000 and renta < 20000:
        return "Le corresponde un impositivo del 15%"
    elif renta >= 20000 and renta < 35000:
        return "Le corresponde un impositivo del 20%"
    elif renta >= 35000 and renta < 60000:
        return "Le corresponde un impositivo del 30%"
    else:
        return "Le corresponde un impositivo del 45%"

def main():
    renta = int(input("Introduce su renta anual: "))
    print(impositivo(renta))

if __name__ == "__main__":
    main()
