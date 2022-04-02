import numpy


def IndexFunc(x, a, b):
    return a * numpy.exp(b * x)


def IndexFunc0(x, b, intercept = 0):
    return intercept * numpy.exp(b * x)


def LinearFunc(x, a, b):
    return a * x + b


def LinearFunc0(x, a, intercept = 0):
    return a * x + intercept


def LogarithmFunc(x, a, b):
    return a * numpy.log(x) + b


def PolynomialFunc_2(x, a, b, c):
    return a * x ** 2 + b * x + c


def PolynomialFunc0_2(x, a, b, intercept = 0):
    return a * x ** 2 + b * x + intercept


def PolynomialFunc_3(x, a, b, c, d):
    return a * x ** 3 + b * x ** 2 + c * x + d


def PolynomialFunc0_3(x, a, b, c, intercept = 0):
    return a * x ** 3 + b * x ** 2 + c * x + intercept


def PolynomialFunc_4(x, a, b, c, d, e):
    return a * x ** 4 + b * x ** 3 + c * x ** 2 + d * x + e


def PolynomialFunc0_4(x, a, b, c, d, intercept = 0):
    return a * x ** 4 + b * x ** 3 + c * x ** 2 + d * x + intercept


def PolynomialFunc_5(x, a, b, c, d, e, f, intercept = 0):
    return a * x ** 5 + b * x ** 4 + c * x ** 3 + d * x ** 2 + e * x + f


def PolynomialFunc0_5(x, a, b, c, d, e, intercept = 0):
    return a * x ** 5 + b * x ** 4 + c * x ** 3 + d * x ** 2 + e * x + intercept


def PowerFunc(x, a, b):
    return a * x ** b


def MyFunc(x, a, b, c):
    return a * x ** b + c


def MyFunc0(x, a, b, intercept = 0):
    return a * b ** x + intercept


def SinFunc(x, a, b, k, c):
    return a*numpy.sin(k*x+b)+c


def SinFunc0(x, a, k, b, intercept = 0):
    return a*numpy.sin(k*x+b) + intercept - a*numpy.sin(b)


def CosFunc(x, a, b, k, c):
    return a*numpy.cos(k*x+b)+c


def CosFunc0(x, a, k, b, intercept = 0):
    return a*numpy.cos(k*x+b) + intercept - a*numpy.cos(b)

class ItemData:
    def __init__(self, x, y, data):
        self.x = x
        self.y = y
        self.data = data

    def __lt__(self, other):
        return self.x < other.x


class PointData:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __lt__(self, other):
        if self.x != other.x:
            return self.x < other.x
        else:
            return self.y < other.y
