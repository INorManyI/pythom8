import collections.abc
'''1'''
def selection_sort(alist):
    if(isinstance(alist, collections.abc.Sequence)):
        for i in range(0, len(alist) - 1):
            smallest = i
            for j in range(i + 1, len(alist)):
                if alist[j] < alist[smallest]:
                    smallest = j
            alist[i], alist[smallest] = alist[smallest], alist[i]
        return alist
    else:
        raise Exception("Не массив")
alist = [1, 3, 2, 4]
selection_sort(alist)
print("1. " + str(alist))


'''2'''
def Polindrom(s):
    # Используем встроенную функцию
    rev = ''.join(reversed(s))
    # Проверяем строки на равенство
    if (s == rev):
        return True
    return False
s = "malayalam"
print("2. " + str(Polindrom(s)))


'''3'''
def fac(n):
    if (n == 1):
        return 1
    elif (n <= 0):
        raise Exception("Нету отрицательного факториала")
    else:
        return (n * fac(n - 1))
print("3. " +str(fac(3)))


'''4'''

def fib(n):
    if (n == 1):
        return 0
    if (n == 2):
        return 1
    if (n < 1):
        raise Exception("Нету отрицательного ряда")
    else:
        return (fib(n - 1) + fib(n - 2))
print("4. " +str(fib(5)))


'''5'''
def step(a,b):
    a= a ** b
    a= float('{:.5f}'.format(a))
    return a
print("5. " +str(step(4.5,1.5)))


'''6'''
def prost(x):
    k = 0;
    for i in range(2, x // 2+1):
        if (x % i == 0):
            k = k+1
    if (k <= 0):
        return True
    else:
        return False
print("6. " +str(prost(15)))

