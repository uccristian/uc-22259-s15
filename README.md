# Suma de $n$ Términos de una Progresión Geométrica: Descarga de Archivos en Cadena

---

## Introducción

Este `README.md` explica el concepto de la **suma de los $n$ términos de una progresión geométrica** a través de un **ejemplo práctico y fácil de entender**: la descarga de archivos donde la velocidad se duplica progresivamente.

---

## ¿Qué es una Progresión Geométrica?

Una progresión geométrica es una secuencia de números donde cada término (después del primero) se obtiene **multiplicando el anterior por una razón constante** ($r$).

---

## La Fórmula para la Suma de los Primeros $n$ Términos ($S_n$)

Para calcular la suma de los primeros $n$ términos de una progresión geométrica, usamos la siguiente fórmula:

$$S_n = \frac{a(r^n - 1)}{r - 1}$$

Donde:
* $S_n$: Es la **suma** de los primeros $n$ términos.
* $a$: Es el **primer término** de la progresión.
* $r$: Es la **razón común** (el factor por el que se multiplica cada término).
* $n$: Es el **número de términos** que queremos sumar.

---

## Ejemplo de Aplicación: Descarga de Archivos en Cadena

### Problema

Imagina que estás descargando un archivo grande de internet. El primer segundo de la descarga, logras bajar **5 kilobytes (KB)**. Sin embargo, tu velocidad de descarga es muy particular: cada segundo subsiguiente, la velocidad de descarga se **duplica** con respecto al segundo anterior.

Si la descarga dura **5 segundos** en total, ¿cuántos **kilobytes en total** habrás descargado al finalizar esos 5 segundos?

### Análisis y Parámetros

La cantidad de KB descargados por segundo forma una **progresión geométrica**:

* **Segundo 1:** 5 KB
* **Segundo 2:** $5 \times 2 = 10$ KB
* **Segundo 3:** $10 \times 2 = 20$ KB
* **Segundo 4:** $20 \times 2 = 40$ KB
* **Segundo 5:** $40 \times 2 = 80$ KB

Para calcular la **cantidad total descargada**, debemos sumar los KB de cada uno de esos 5 segundos.

Según nuestra fórmula, los parámetros son:
* **Primer término ($a$):** 5 KB (la cantidad descargada en el primer segundo).
* **Razón ($r$):** 2 (la velocidad se duplica cada segundo).
* **Número de términos ($n$):** 5 (la descarga dura 5 segundos).

### Cálculo del Resultado

Aplicando la fórmula $S_n = \frac{a(r^n - 1)}{r - 1}$:

$S_5 = \frac{5(2^5 - 1)}{2 - 1}$
$S_5 = \frac{5(32 - 1)}{1}$
$S_5 = 5 \times 31$
$S_5 = 155$ KB

### Interpretación del Resultado

El resultado del cálculo es que la cantidad **total de kilobytes descargados es de 155 KB**.
