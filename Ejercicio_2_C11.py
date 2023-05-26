def crear_cadena () -> str :

    cadena : str = input("Ingrese su cadena: ")

    return (cadena)

def cadena_inversa (cadena : str) -> None :

    if (cadena == cadena[::-1]):
        print(f"La cadena es igual a su inversa '{cadena[::-1]}'.")
    else:
        print("La cadena no es igual a su inversa.")

    return (None)

def main () -> None :

    cadena : str = crear_cadena()
    cadena_inversa(cadena)

    return (None)

main()