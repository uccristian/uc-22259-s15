def factorialn(n):
    if n == 0:
        return 1
    else:
        return n * factorialn(n - 1)

def factorialk(k):
    if k == 0:
        return 1
    else:
        return k * factorialk(k - 1)

def Ejecutor():
    while True:
        n = int(input("Ingrese el valor de n (mayor o igual que 0): "))
        k = int(input("Ingrese el valor de k (mayor o igual que 0): "))

        if n < 0 or k < 0:
            print("ERROR. Vuelva a ingresar")
        elif k > n:
            print("ERROR: k no puede ser mayor que n. Intente de nuevo.")
        else:
            break

    fn = factorialn(n)
    fk = factorialk(k)
    fnk = factorialn(n - k)

    combinacion = fn // (fk * fnk)

    print(f"C({n}, {k}) = {combinacion}")


Ejecutor()