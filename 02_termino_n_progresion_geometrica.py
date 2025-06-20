ProgresionesCalculadas = 0
TotalTerminos = 0

def Salir():
    print("Gracias por usar la calculadora. ¡Hasta luego!")

def Reportar():
    print("\n=========== REPORTE ===========\n")
    print("Total de cálculos realizados:\t\t", ProgresionesCalculadas)
    print("Suma de todos los términos calculados:\t", TotalTerminos)

def CalcularTermino(a1, r, n):
    return a1 * (r ** (n - 1))

def Procesar():
    global ProgresionesCalculadas, TotalTerminos

    a1 = float(input("Ingrese el primer término de la sucesión (a1): "))
    r = float(input("Ingrese la razón (r): "))

    while True:
        n = int(input("Ingrese la posición del término a calcular (n): "))
        if n >= 1:
            break
        print("Error: n debe ser 1 o mayor")

    termino = CalcularTermino(a1, r, n)
    ProgresionesCalculadas += 1
    TotalTerminos += termino

    print(f"\nEl término {n} es: {termino:.4f}")

def Menu():
    print("\n=========== MENU OPCIONES ===========\n")
    print("1. Procesar la Progresion Geometrica")
    print("2. Reportar")
    print("3. Salir")

    while True:
        op = int(input("Ingrese opcion de menú:\t\t"))

        if (op < 1 or op > 3):
            print("ERROR. Vuelva a ingresar")
        else:
            break

    match op:
        case 1: Procesar()
        case 2: Reportar()
        case 3: Salir()

    return op

def Ejecutar():
    while True:
        opcion = Menu()
        if (opcion == 3):
            break

Ejecutar()