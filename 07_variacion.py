import math

def calcular_variaciones(n, k):

    if not isinstance(n, int) or not isinstance(k, int):
        raise TypeError("n y k deben ser números enteros.")
    if n < 0 or k < 0:
        raise ValueError("n y k no pueden ser números negativos.")
    if k > n:
        return 0 

    # Calculamos n!
    factorial_n = math.factorial(n)
    
    # Calculamos (n-k)!
    factorial_n_menos_k = math.factorial(n - k)
    
    # El resultado de la variación
    variaciones = factorial_n // factorial_n_menos_k
    
    return variaciones
    

n1 = int(input("Ingresar el numero total de elementos: "))
k1 = int(input("Ingresar el numero de elementos que se van a seleccionar y ordenar: "))
resultado1 = calcular_variaciones(n1, k1)
print(f"V({n1}, {k1}) = {resultado1}")
