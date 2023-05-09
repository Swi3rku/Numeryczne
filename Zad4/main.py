import math
from horner import horner
import numpy as np

#==============================#
#                              #
#  Code By string(74*83)(1+')  #
#                              #
#==============================#

def hermiteFunc(x):
    return pow(math.e,-x**2)

def zlozenie (function):
    def func(x):
        return function(x)*hermiteFunc(x)
    return func


def f(x):
    return horner(x,[1,0,1,0,60],5)
    # return x**2+x**4+60
def g(x):
    return (x * np.sin(x) ** 2)
def funMod(x):
    return abs(abs(x-4)-5)
def notFunLine(x):
    return 3*x-5

def simpson(f, a, b):
    wynik = ((b-a)/6)*(f(a)+4*f((a+b)/2)+f(b))
    return wynik

def h(x):
    return np.sin(x) + np.sin(3*x) + np.sin(5*x)

#==============================#
#                              #
#  Code By string(74*83)(1+')  #
#                              #
#==============================#
def podzielNaPrzedzialy(a,b,liczbaPrzedzialow):
    przedzialy = []
    przesuniecie = (b-a)/liczbaPrzedzialow
    for i in range(liczbaPrzedzialow):
        tmp = (a, a+przesuniecie)
        przedzialy.append(tmp)
        a = a+przesuniecie
    return przedzialy

def newtonCotes(f, a, b, dokladnosc):
    liczbaPrzedzialow = 1
    poprzedniWynik = 0
    wynik = 0
    czyPierwszyRaz = True
    while(abs(poprzedniWynik-wynik)>dokladnosc or czyPierwszyRaz):
        poprzedniWynik = wynik
        wynik = 0
        czyPierwszyRaz = False
        przedzialy = podzielNaPrzedzialy(a,b,liczbaPrzedzialow)
        for i in range(liczbaPrzedzialow):
            wynik += simpson(f,przedzialy[i][0],przedzialy[i][1])
        liczbaPrzedzialow = liczbaPrzedzialow * 2
    return wynik

def newtonCotesInf(f, step, dokladnosc):
    wynikDod=0
    a,b=0,1

    czyPierwszyRazDod = True
    while(True):
        obliczoneDod=simpson(f,a,b)
        wynikDod+=obliczoneDod
        a,b=b,b+step
        if(abs(obliczoneDod)<=dokladnosc):
            break

    obliczoneUj=-10
    wynikUj=0
    a,b=-1,0
    czyPierwszyRazUj=True
    while(abs(obliczoneUj) > dokladnosc or czyPierwszyRazUj):
        czyPierwszyRazUj=False
        obliczoneUj=simpson(f,a,b)
        wynikUj+=obliczoneUj
        a,b=a-step,a

    return wynikUj+wynikDod
#==============================#
#                              #
#  Code By string(74*83)(1+')  #
#                              #
#==============================#
def gaussHermite(f, n):
    wynik = 0
    if n == 2:
        x, a = [0.88622692, 0.88622692], [-0.70710678, 0.70710678]
    elif n == 3:
        x, a = [0.29540897, 1.18163590, 0.29540897], [-1.22474487, 0.00000000, 1.22474487]
    elif n == 4:
        x, a = [0.08131283, 0.80491409, 0.80491409, 0.08131283], [-1.65068012, -0.52464762, 0.52464762, 1.65068012]
    elif n == 5:
        x, a = [0.01995324, 0.39361932, 0.94530872, 0.39361932, 0.01995324], [-2.02018287, -0.95857246, 0.00000000, 0.95857246, 2.02018287]
    for i in range(n):
        wynik += x[i] * f(a[i])
    return wynik

#==============================#
#                              #
#  Code By string(74*83)(1+')  #
#                              #
#==============================#
zbiorFunc=[f, g, h, funMod, notFunLine]
functions = [
    "x^4 + x^2 + 60",
    "(x * sin(x) ^ 2)",
    "||x - 4| - 5|",
    "3*x - 5"
]
print("Podaj dokładość dla Newtona-Cotesa: ")
dokladnosc=float(input())
print("Podaj wartość kroku dla Newtona-Cotesa: ")
krok=float(input())
print("Podaj N dla Gaussa-Hermite'a: ")
n=int(input())
for i in range(len(zbiorFunc)-1):
    print("Wartość całki funkcji ",functions[i]," metodą Newtona-Cotesa dla dokładnosci: ",dokladnosc," i kroku: ",krok,": ",newtonCotesInf(zlozenie(zbiorFunc[i]),krok,dokladnosc))
    print("Wartość całki funkcji ",functions[i]," metodą Gaussa-Hermite'a dla N=",n,": ",gaussHermite(zbiorFunc[i],n))

#==============================#
#                              #
#  Code By string(74*83)(1+')  #
#                              #
#==============================#