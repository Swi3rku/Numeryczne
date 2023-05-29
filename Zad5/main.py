# from horner import horner
import matplotlib.pyplot as plt
import sympy as sym
from Zad5.calki import *
import numpy as np
import math


def f(x):
    # return horner(x,[1,0,1,0,60],5)
    return x**2+x**4+60


def g(x):
    # return (x * np.sin(x) ** 2)
    return (2*x**3 * np.sin(3*x) ** 2 + 1)


def funMod(x):
    return abs(abs(x-4)-5)
    # return np.cos(np.sin(3*x))


def notFunLine(x):
    return 3*x-5


def testFun(x):
    return abs(x)
    # return 2*x**2+x-2
    # return np.sin(x) #chyba jako tako dziala
    # return np.cos(2*x**2+1)

def menu():
    print("1. x^4+x^2+60"
          "2. 2x^3*sin^2(3x)+1"
          "3. ||x-4|-5|"
          "4. 3x-5")
    print("wybor: ")
    wybor = int(input())


def wielomiany(n, x):
    if n == 0:
        return 1 + 0*x
    elif n == 1:
        return 2*x;
    else:
        return 2*x*wielomiany(n-1, x) - 2*(n-1)*wielomiany(n-2, x)


def aproks(funkcja, stopienWielomianu, iloscWezlow, przedzialA, przedzialB):
    wynik = 0
    zakres = np.linspace(przedzialA, przedzialB)
    for i in range(stopienWielomianu + 1):
        tmp = wielomiany(i,zakres)
        wsp = (1/(math.sqrt(math.pi)*(2**i)*math.factorial(i)))*gaussHermite(funkcja,iloscWezlow,i)
        wynik += tmp*wsp
    return wynik


a = -2
b = 2
przedzial = np.linspace(a,b)
# print(aproks(testFun,2,5,-2,2))
# print(wielomiany(3,przedzial))
plt.plot(przedzial, aproks(testFun,5,5,a,b))
plt.plot(przedzial, testFun(przedzial), linestyle='dashed', color='red')

# x = sym.Symbol('x')
# for i in range(5):
#     print(wielomiany(i,x))
