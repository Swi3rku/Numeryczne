import math
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 3 * x ** 2 - 3 * x - 1

def g(x):
    print("funkcja ", math.sin(4*x))
    return math.sin(4*x)

def h(x):
    return 1

def bisekcja(przedzialA, przedzialB, liczbaIteracji, dokladnosc,func):
    #warunek końca: dokładność
    if(liczbaIteracji==-1):
        x = (przedzialA + przedzialB) / 2
        poprzedniaWartosc = 0
        while(abs(x-poprzedniaWartosc) > dokladnosc):
            if func(x) * func(przedzialA) > 0:
                przedzialA = x
            else:
                przedzialB = x
            poprzedniaWartosc=x
            x = (przedzialA + przedzialB) / 2
    #warunek końca: liczba iteracji
    else:
        for i in range(1, liczbaIteracji):
            x = (przedzialA + przedzialB) / 2
            if func(x) * func(przedzialA) > 0:
                przedzialA = x
            else:
                przedzialB = x
    print("Miejsce zerowe: ",x)
    pom=np.linspace(-5,5,100)
    plt.plot(pom,  func(pom),'r')
    plt.plot(pom, 0*pom,'r')
    plt.show()


def sieczne(przedzialA, przedzialB, liczbaIteracji, dokladnosc, func):
    #przypisanie końców przedziału do x
    x=[przedzialA,przedzialB]
    pr=przedzialA
    # wzór do liczenia stycznych
    for i in range(0,liczbaIteracji-1):
        st=(( func(x[0])*x[1] )-( func(x[1])*x[0] ))/(func(x[0])-func(x[1]))
        #st=przedzialA
        if (abs(st-pr)<dokladnosc):
            print("miejsce zerowe: ",st)
            pom=np.linspace(przedzialA,przedzialB,100)
            plt.plot(pom,  func(pom),'r')
            plt.plot(pom, 0*pom,'r')
            plt.show()
            return
        pr=st
        x[0],x[1]=st,x[0]
        if(x[0]>x[1]):
            x[0],x[1]=x[1],x[0]
            

    # TODO sprawdzić czy st wystarczająco bliskie 0,
    # jeśli nie to zamienić x[0] z x[1] i za x[1] podstawić st

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
    poczatekPrzedzialu= int(input())
    print("Podaj końcową wartość przedziału: ")
    koniecPrzedzialu= int(input())
    return poczatekPrzedzialu, koniecPrzedzialu

def menuDokladnosc():
    print("Podaj dokładność: ")
    dokladnosc= float(input())
    return dokladnosc
    
def menuLiczbaIteracji():
    print("Podaj liczbe iteracji: ")
    liczbaIteracji= int(input())
    return liczbaIteracji

def menu():
    wybor=0
    listaFunkcji=[f,g,h]
    while(wybor!=9):
        print("1. Dokładność")
        print("2. Liczba iteracji")
        print("9. Koniec psot")
        print("Podaj warunek stopu: ")
        wybor = int(input())
        print("Wybierz funkcje:")
        print("1. 3x^2-3x-1\n"
              "2. sin(4x)\n"
              "3. work in progress")
        funkcja = int(input())
        if(wybor==1):
            a,b = menuPrzedzial()
            epsilon = menuDokladnosc()
            wrap(a,b,-1,epsilon,listaFunkcji[funkcja-1])
        elif(wybor==2):
            a,b = menuPrzedzial()
            iteracje = menuLiczbaIteracji()
            wrap(a,b, iteracje,-1,listaFunkcji[funkcja-1])



menu()
