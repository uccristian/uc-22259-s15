def factorial(n):
    if n < 0:
        raise TypeError("n debe ser mayor de 0")

    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
n = int(input("Ingresar numero: "))
factorial1 = factorial(n)
print(f"El factorial de {n} es {factorial(n)}")