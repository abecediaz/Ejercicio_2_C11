def imprimir_menu () -> None :

    print("\n")
    print("Menú:")
    print("1) ¿La cadena es igual a su inversa?")
    print("2) Dar vuelta la cadena")
    print("\n")

    return (None)

def ingresar_opcion () -> str :

    imprimir_menu()

    op : str = input("Ingrese el número correspondiente a la opción que quiera realizar: ")
    while validar_opcion(op):
        op : str = input(f"El término que ingresó, '{op}' no es válido. Inténtelo de nuevo: ")

    return (op)

def validar_opcion (op : str) -> bool :

    if (op not in ["1", "2"]):
        return (True)

    else:
        return (False)

def verificar_cadena_inversa (cadena : str) -> None :

    if (cadena == cadena[::-1]):
        print(f"La cadena '{cadena.upper()}' es igual a su inversa '{cadena[::-1].upper()}'.")
    else:
        print("La cadena no es igual a su inversa.")

    return (None)

def invertir_cadena (cadena : str) -> None :

    print(f"La cadena espejada queda: '{cadena[::-1]}'.")

    return ()

def main () -> None :

    op : str = ingresar_opcion()

    cadena : str = input("Ingrese su cadena: ").lower()

    if (op == "1"):
        verificar_cadena_inversa(cadena)
    else:
        invertir_cadena(cadena)

    return (None)

main()