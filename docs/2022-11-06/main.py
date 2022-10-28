"""This is a very short docstring."""

a = 4
b = 5.5
c = 1.5 + 2j
d = "a"
e = 6.0 * a - b * b + c ** (a + b + c)
a, b, c, d, e

if __name__ == "__main__":
    pass

x: float = 0.47
if 0 < x < 1:
    print(f"{x} cae entre 0 y 1.")
elif 1 < x < 2:
    print(f"{x} cae entre 1 y 2.")
else:
    pass
