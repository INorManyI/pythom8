from math import inf

def abs(n):
    if n < 0:
        return -n
    return n

def factorial(n):
    if n < 0:
        raise Exception("Нету отрицательного факториала")
    if n <= 1:
        return 1
    return (n * factorial(n - 1))

def cos(x) :
    result = 0
    n = 0
    delta = pow(-1, n) * pow(x, 2 * n) / factorial(2 * n)
    minDelta = 0.0000001
    while abs(delta) > minDelta:
        delta = pow(-1, n) * pow(x, 2 * n) / factorial(2 * n)
        result = result + delta
        n = n + 1
    return result

def ln(x) :
    if x < 0.0:
        raise Exception("ERROR: given negative number: " + x)
    if x == 0.0:
        return inf
    result = 0.0
    n = 0.0
    a = 2 * n + 1
    delta = 2 * (1.0 / a) * pow((x - 1) / (x + 1), a)
    minDelta = 0.000000001
    while abs(delta) > minDelta:
        n = n + 1
        a = 2 * n + 1
        result = result + delta
        delta = 2 * (1.0 / a) * pow((x - 1) / (x + 1), a)
    return result

def sin(x):
    result = 0
    n = 0
    delta = pow(-1, n) * pow(x, 2 * n + 1) / factorial(2 * n + 1)
    minDelta = 0.0000001
    while abs(delta) > minDelta:
        delta = pow(-1, n) * pow(x, 2 * n + 1) / factorial(2 * n + 1)
        result = result + delta
        n = n + 1
    return result

def func(x):
    if x == 0:
        return inf
    if x > 0:
        return ln(x) * cos(x);
    if x < 0:
        return abs(sin(x)-cos(x)) / ln(abs(x));
