def Func(number):
    total = 0
    while number > 0:
        total = total + number * (number - 1)
        number = number - 1
    return total
