def suma_progresion_geometrica(primer_termino, razon, numero_terminos):
    if razon == 1:
        return primer_termino * numero_terminos
    else:
        suma = (primer_termino * ((razon**numero_terminos) - 1)) / (razon - 1)
        return suma

a = 5  # Primer término
r = 2  # Razón
n = 6  # Número de términos a sumar

resultado_suma = suma_progresion_geometrica(a, r, n)
print(f"\nLa cantidad total de kilobytes descargados despues de {n} segundos es: {resultado_suma}")
