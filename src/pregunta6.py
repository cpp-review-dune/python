#!/usr/bin/env python


"""
Considere un triángulo con lados de longitud 3u, 7u y 9u.
La ley de cosenos establece que dados los tres lados de un triángulo
a, b y c, el ángulo C entre los lados a y b es
c**2 = a**2 + b**2 - 2ab cos (C).
Escriba un programa en Python para calcular los tres ángulos en el
triángulo.
"""


def cosine_law(a: float, b: float, c: float) -> float:
    """Retorna el ángulo C entre los lados a y b.

    Args:
        a (float): lado a.
        b (float): lado b.
        c (float): lado c opuesto al ángulo C.

    Returns:
        float: ángulo C en radianes.
    """
    from math import acos

    """Verificar la desigualdad triangular."""
    assert 0 < a < b + c, f"{a} < {b} + {c} no es correcto."
    assert 0 < b < a + c, f"{b} < {a} + {c} no es correcto."
    assert 0 < c < a + b, f"{c} < {a} + {b} no es correcto."

    return acos((a**2 + b**2 - c**2) / (2 * a * b))


if __name__ == "__main__":
    lado_A, lado_B, lado_C = 3.0, 7.0, 9.0
    A = cosine_law(a=lado_B, b=lado_C, c=lado_A)
    B = cosine_law(a=lado_A, b=lado_C, c=lado_B)
    C = cosine_law(a=lado_A, b=lado_B, c=lado_C)
    message = f"Los ángulos del triángulo son {A}, {B} y {C} \
y suman {A + B + C} radianes."
    print(message)
