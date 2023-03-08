import math
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 3 * x ** 2 - 3 * x - 1

def g(x):
    return math.sin(4*x)

def h(x):
    return 1

def bisekcja(przedzialA, przedzialB, liczbaIteracji, dokladnosc):
    if (przedzialA>przedzialB):
        przedzialA, przedzialB = przedzialB, przedzialA
    #warunek końca: dokładność
    if(liczbaIteracji==-1):
        x = (przedzialA + przedzialB) / 2
        poprzedniaWartosc = 0
        while(abs(x-poprzedniaWartosc) > dokladnosc):
            if f(x) * f(przedzialA) > 0:
                przedzialA = x
            else:
                przedzialB = x
            poprzedniaWartosc=x
            x = (przedzialA + przedzialB) / 2
    #warunek końca: liczba iteracji
    else:
        for i in range(1, liczbaIteracji):
            x = (przedzialA + przedzialB) / 2
            if f(x) * f(przedzialA) > 0:
                przedzialA = x
            else:
                przedzialB = x
    print("Miejsce zerowe: ",x)
    pom=np.linspace(-5,5,100)
    plt.plot(pom,  f(pom),'r')
    plt.plot(pom, 0*pom,'r')
    plt.show()

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
    while(wybor!=9):
        print("1. Dokładność")
        print("2. Liczba iteracji")
        print("9. Koniec psot")
        print("Podaj warunek stopu: ")
        wybor = int(input())
        if(wybor==1):
            a,b = menuPrzedzial()
            epsilon = menuDokladnosc()
            bisekcja(a,b,-1,epsilon)
            #siecznych()
        elif(wybor==2):
            a,b = menuPrzedzial()
            iteracje = menuLiczbaIteracji()
            bisekcja(a,b,iteracje, -1)
            #siecznych()



menu()