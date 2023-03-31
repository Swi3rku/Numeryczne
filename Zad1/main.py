import numpy as np
from horner import horner
from bisekcja import bisekcja
from sieczne import sieczne


def f(x):
    return horner(x, [5, -7, 1, -1], 4)


def g(x):
    return np.sin(4 * x)


def h(x):
    return 2 ** (x + 1) - 3


# Funkcja sprawdzająca podstawowe warunki do użycia metod bisekcji i siecznych
def wrap(przedzialA, przedzialB, liczbaIteracji, dokladnosc, func):
    if (przedzialA == przedzialB):
        print("Początek i koniec przedziału są sobie równe")
        return
    if (przedzialA > przedzialB):
        przedzialA, przedzialB = przedzialB, przedzialA

    bisekcja(przedzialA, przedzialB, liczbaIteracji, dokladnosc, func)
    sieczne(przedzialA, przedzialB, liczbaIteracji, dokladnosc, func)


def menuPrzedzial():
    print("Podaj początkową wartość przedziału: ")
    poczatekPrzedzialu = float(input())
    print("Podaj końcową wartość przedziału: ")
    koniecPrzedzialu = float(input())
    return poczatekPrzedzialu, koniecPrzedzialu


def menuDokladnosc():
    print("Podaj dokładność: ")
    dokladnosc = float(input())
    return dokladnosc


def menuLiczbaIteracji():
    print("Podaj liczbe iteracji: ")
    liczbaIteracji = int(input())
    return liczbaIteracji


def wyborFunkcji():
    print("Wybierz funkcje:")
    print("1. 5x^3-7x^2+x-1\n"
          "2. sin(4x)\n"
          "3. 2^(x+1)-3")
    funkcja = int(input())
    return funkcja


def menu():
    wybor = 0
    listaFunkcji = [f, g, h]
    while (wybor != 9):
        print("=======================")
        print("1. Dokładność")
        print("2. Liczba iteracji")
        print("9. Koniec psot")
        print("Podaj warunek stopu")
        print("=======================")
        wybor = int(input())
        if (wybor == 1):
            funkcja = wyborFunkcji()
            a, b = menuPrzedzial()
            epsilon = menuDokladnosc()
            wrap(a, b, -1, epsilon, listaFunkcji[funkcja - 1])
        elif (wybor == 2):
            funkcja = wyborFunkcji()
            a, b = menuPrzedzial()
            iteracje = menuLiczbaIteracji()
            wrap(a, b, iteracje, -1, listaFunkcji[funkcja - 1])


menu()
