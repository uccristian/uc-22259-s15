def suma_progresion_geometrica(primer_termino, razon, numero_terminos):
    if razon == 1:
        return primer_termino * numero_terminos
    else:
        suma = (primer_termino * ((razon**numero_terminos) - 1)) / (razon - 1)
        return suma

a = 0.1     # Primer término
r = 2       # Razón
n = 5       # Número de términos a sumar

resultado_suma = suma_progresion_geometrica(a, r, n)
print(resultado_suma)




