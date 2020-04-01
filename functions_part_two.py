import math


def f(x):
    if x >= 100:
        return 2 * x + 10
    else:
        return x / 2 + 10


# print(f(99))


def sqr(x):
    return x ** (1 / 2)


def power_of(base, exponent):
    return base ** exponent


def funny_function(temperature, humidity):
    if temperature < 30 and humidity >= 70:
        return (temperature / (2 * humidity)) * math.e
    elif temperature <= 5 and humidity == 0:
        return sqr(temperature + humidity) / (2 * math.e)
    elif temperature >= 30 and humidity < 70 and humidity != 0:
        return power_of(temperature, math.e) / (2 * humidity * math.e)
    return 0.0


print(funny_function(15, 90))
print(funny_function(-15, 0))
print(funny_function(30, 3))
