def calcular_termino_aritmetico(a1, d, n):
    "Calcula el término n-ésimo de una progresión aritmética. Fórmula: an = a1 + (n - 1) * d"
    an = a1 + (n - 1) * d
    return an


# Entrada de datos
print("Cálculo del término n-ésimo de una progresión aritmética")
a1 = float(input("Ingrese el primer término (a1): "))
d = float(input("Ingrese la diferencia común (d): "))
n = int(input("Ingrese el número del término que desea encontrar (n): "))

# Cálculo
termino = calcular_termino_aritmetico(a1, d, n)

# Salida
print(f"El término número {n} de la progresión aritmética es: {termino}")
