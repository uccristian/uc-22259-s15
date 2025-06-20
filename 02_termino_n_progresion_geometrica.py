def CalcularTermino(a1, r, n):
    return a1 * (r ** (n - 1))

def Procesar():
    a1 = float(input("Ingrese el primer término de la sucesión (a1): "))
    r = float(input("Ingrese la razón (r): "))

    while True:
        n = int(input("Ingrese la posición del término a calcular (n): "))
        if n >= 1:
            break
        print("Error: n debe ser 1 o mayor")

    termino = CalcularTermino(a1, r, n)

    print(f"\nEl término {n} es: {termino}")

Procesar()