import  math
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 0.5 * x ** 2 + 0.5 * x - 0.5

def g(x):
    return math.sin(4*x)

def h(x):
    return math.cos(3*x)+1

def bisekcja(przedzialA, przedzialB, liczbaIteracji, dokladnosc,func):
    if (przedzialA>przedzialB):
        przedzialA, przedzialB = przedzialB, przedzialA
    for k in range(1, liczbaIteracji):
        x = (przedzialA + przedzialB) / 2
        if abs(func(x)) < dokladnosc:
            break
        else:
            if func(x) * func(przedzialA) < 0:
                przedzialB = x
            else:
                przedzialA = x
    print("Mijesce zerowe: ",x)
    pom=np.linspace(-10,10,100)
    # pom2=
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
    if ( func(przedzialA)*(func(przedzialB))>=0.0):
        print("Wartość funkcji na krańcach przedziału nie są różnych znaków")
        return

    bisekcja(przedzialA, przedzialB, liczbaIteracji, dokladnosc, func)
    sieczne(przedzialA, przedzialB, liczbaIteracji, dokladnosc, func)

def menuBisekcji():
    print("Podaj początkową wartość przedziału: ")
    poczatekPrzedzialu= input()
    print("Podaj końcową wartość przedziału: ")
    koniecPrzedzialu= input()
    print("Podaj liczbe iteracji: ")
    liczbaIteracji= input()
    print("Podaj dokłądność: ")
    dokladnosc= input()
    wrap(int(poczatekPrzedzialu),int(koniecPrzedzialu),int(liczbaIteracji),float(dokladnosc),f)

def menu():
    wybor=0
    while(wybor!=9):
        print("1. Metoda bisekcji")
        print("2. Metoda siecznych")
        print("9. Koniec psot")
        wybor = int(input())
        if(wybor==1):
            menuBisekcji()
        elif(wybor==2):
            print("Work in progress!")

menu()
