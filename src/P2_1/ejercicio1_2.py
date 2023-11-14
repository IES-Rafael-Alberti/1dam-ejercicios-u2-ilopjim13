def pasar(contra):
    psw = "contraseña"
    if psw == contra:
        return "La contraseña es correcta."
    else:
        return "La contraseña es incorrecta"

def main():
    contra = input("Introduce la contraseña: ")
    print(pasar(contra))

if __name__ == "__main__":
    main()

