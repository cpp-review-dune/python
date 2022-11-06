#!/usr/bin/env python


# Calcular la longitud y aŕea de una círculo a partir de su radio
# Paso 1: Pida el radio del círculo.
# Paso 2: Aplique las fórmulas.
# Paso 3: Imprima los resultados.
import math

radius_str = input("Ingrese el radio de tu círculo: ")
radius_float = float(radius_str)

lenght = 2 * math.pi * radius_float
area = math.pi * (radius_float**2)

message = f"La longitud del círculo es {lenght:.2f}u \
y su área es {area:.2f}u^2"

print(message)
