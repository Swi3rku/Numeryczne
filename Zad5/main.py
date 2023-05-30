# from horner import horner
import matplotlib.pyplot as plt
import sympy as sym
from Zad5.calki import *
import numpy as np
import math


#=====================================#
#                                     #
#  Code By string(74)string(83)(1+')  #
#                                     #
#=====================================#


def funPol(x):
    # return horner(x,[1,0,1,0,60],5)
    return x**2+x**4+60


def notFunPol(x):
    return -x**2


def notFunLine(x):
    return 3*x-5


def funCos(x):
    return np.cos(2*x**2+1)


def notFunsin(x):
    return np.sin(x)


def funMod(x):
    return abs(abs(x-4)-5)


def notFunMod(x):
    return abs(x)


def superUltraTurboFun(x):
    return funCos(funMod(x))


#=====================================#
#                                     #
#  Code By string(74)string(83)(1+')  #
#                                     #
#=====================================#


def wielomiany(n, x):
    if n == 0:
        return 1 + 0*x
    elif n == 1:
        return 2*x
    else:
        wyniki = [1 + 0*x, 2*x]
        for i in range(2, n + 1):
            wyniki.append(2*x*wyniki[i-1] - 2*(i-1)*wyniki[i-2])
        return wyniki[n]


def aproks(funkcja, stopienWielomianu, iloscWezlow, przedzialA, przedzialB):
    wynik = 0
    zakres = np.linspace(przedzialA, przedzialB)
    for i in range(stopienWielomianu + 1):
        tmp = wielomiany(i,zakres)
        wsp = (1/(math.sqrt(math.pi)*(2**i)*math.factorial(i)))*gaussHermite(funkcja,iloscWezlow,i)
        wynik += tmp*wsp
    return wynik


def blad(pierwotne_wartosci, aproksymowane_wartosci):
    n = len(pierwotne_wartosci)
    suma_kwadratow = sum((pierwotne_wartosci[i] - aproksymowane_wartosci[i]) ** 2 for i in range(n))
    blad_aproksymacji = (suma_kwadratow)/n
    return blad_aproksymacji


#=====================================#
#                                     #
#  Code By string(74)string(83)(1+')  #
#                                     #
#=====================================#


a = -2
b = 2
przedzial = np.linspace(a,b)
listaF = [funPol, notFunPol, funCos, notFunsin, funMod, notFunMod, notFunLine,superUltraTurboFun]
f = open(".\\blad.txt","a")
for i in listaF:
    plt.figure(figsize=(4,3),dpi=300)
    plt.plot(przedzial, aproks(i,2,5,a,b))
    plt.plot(przedzial, i(przedzial), linestyle='dashed', color='red')
    plt.title(f"{i.__name__}, stopień: 2")
    print(blad(i(przedzial), aproks(i,2,5,a,b)))
    plt.savefig(f"wykres{i.__name__}2.png")
    plt.show()
    f.write(f"{i.__name__}, 2, \t{blad(i(przedzial), aproks(i,2,5,a,b))}\n")
    #*************
    plt.figure(figsize=(4,3),dpi=300)
    plt.plot(przedzial, aproks(i,5,5,a,b))
    plt.plot(przedzial, i(przedzial), linestyle='dashed', color='red')
    plt.title(f"{i.__name__}, stopień: 5")
    print(blad(i(przedzial), aproks(i,5,5,a,b)))
    plt.savefig(f"wykres{i.__name__}5.png")
    plt.show()
    f.write(f"{i.__name__}, 5, \t{blad(i(przedzial), aproks(i,5,5,a,b))}\n")

f.close()


#=====================================#
#                                     #
#  Code By string(74)string(83)(1+')  #
#                                     #
#=====================================#