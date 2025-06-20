def sumaProgresionAritmetica(a, d, n):
    suma = (n / 2) * (2 * a + (n - 1) * d)
    return suma

a = int(input("Ingrese el primer término (a):\t"))
d = int(input("Ingrese la diferencia común (d):\t"))
n = int(input("Ingrese el número de términos (n):\t"))

resultado = sumaProgresionAritmetica(a, d, n)
print(f"La suma de los primeros {n} términos es: {resultado}")