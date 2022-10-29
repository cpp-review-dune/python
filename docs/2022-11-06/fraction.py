from fractions import Fraction

if __name__ == "__main__":
    a = Fraction(3, 7)
    b = Fraction(24, 56)

    print(f"a.num = {a.numerator}, b.den = {b.denominator}")
    print(a, b)
    print(f"Floating point of a is: {float(a)}")
    print(a + b)
    print(f"Product {a*b}, Sum {a+b}")
