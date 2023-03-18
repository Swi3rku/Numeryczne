import math
import matplotlib.pyplot as plt
import numpy as np
from horner import horner
from bisekcja import bisekcja
from sieczne import sieczne

def f(x):
    #ta funkcja chyba nie ma miejsc zerowych więc podmieniłem na:
    #x**2+x-1
    #return 3 * x ** 2 - 3 * x - 1
    return horner(x, [1,1,-1], 3)

def g(x):
    # print("x= ",x, "sin(4x)", math.sin(4*x))
    return np.sin(4*x)

def h(x):
    return 2**x-1

# Funkcja sprawdzająca podstawowe warunki do użycia metod bisekcji i siecznych
def wrap(przedzialA, przedzialB, liczbaIteracji, dokladnosc, func):
    if (przedzialA==przedzialB):
        print("Początek i koniec przedziału są sobie równe")
        return
    if (przedzialA > przedzialB):
        przedzialA, przedzialB = przedzialB, przedzialA
    # sprawdzanie czy func(x[0]) i func(x[1]) są różne znaki
    if (func(przedzialA)*(func(przedzialB))>=0):
        print("Wartość funkcji na krańcach przedziału nie są różnych znaków")
        return

    bisekcja(przedzialA, przedzialB, liczbaIteracji, dokladnosc, func)
    sieczne(przedzialA, przedzialB, liczbaIteracji, dokladnosc, func)

def menuPrzedzial():
    print("Podaj początkową wartość przedziału: ")
    poczatekPrzedzialu= float(input())
    print("Podaj końcową wartość przedziału: ")
    koniecPrzedzialu= float(input())
    return poczatekPrzedzialu, koniecPrzedzialu

def menuDokladnosc():
    print("Podaj dokładność: ")
    dokladnosc= float(input())
    return dokladnosc
    
def menuLiczbaIteracji():
    print("Podaj liczbe iteracji: ")
    liczbaIteracji= int(input())
    return liczbaIteracji

def wyborFunkcji():
    print("Wybierz funkcje:")
    print("1. 3x^2-3x-1\n"
          "2. sin(4x)\n"
          "3. work in progress")
    funkcja = int(input())
    return funkcja

def menu():
    wybor=0
    listaFunkcji=[f,g,h]
    while(wybor!=9):
        print("=======================")
        print("1. Dokładność")
        print("2. Liczba iteracji")
        print("9. Koniec psot")
        print("Podaj warunek stopu")
        print("=======================")
        wybor = int(input())
        if(wybor==1):
            funkcja = wyborFunkcji()
            a,b = menuPrzedzial()
            epsilon = menuDokladnosc()
            wrap(a,b,-1,epsilon,listaFunkcji[funkcja-1])
        elif(wybor==2):
            funkcja = wyborFunkcji()
            a,b = menuPrzedzial()
            iteracje = menuLiczbaIteracji()
            wrap(a,b, iteracje,-1,listaFunkcji[funkcja-1])

# menu()
sieczne(0,5,-1,0.0001,h)
bisekcja(0,5,-1,0.0001,h)