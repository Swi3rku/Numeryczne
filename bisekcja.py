import  math
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 0.5 * x ** 2 + 0.5 * x - 0.5

def g(x):
    return math.sin(4*x)

def h(x):
    return math.cos(3*x)+1

def bisekcja(przedzialA, przedzialB, liczbaIteracji, dokladnosc):
    if (przedzialA>przedzialB):
        przedzialA, przedzialB = przedzialB, przedzialA
    for k in range(1, liczbaIteracji):
        x = (przedzialA + przedzialB) / 2
        if abs(f(x)) < dokladnosc:
            break
        else:
            if f(x) * f(przedzialA) < 0:
                przedzialB = x
            else:
                przedzialA = x
    print("Mijesce zerowe: ",x)
    pom=np.linspace(-10,10,100)
    # pom2=
    plt.plot(pom,  f(pom),'r')
    plt.plot(pom, 0*pom,'r')
    plt.show()

def menuBisekcji():
    print("Podaj początkową wartość przedziału: ")
    poczatekPrzedzialu= input()
    print("Podaj końcową wartość przedziału: ")
    koniecPrzedzialu= input()
    print("Podaj liczbe iteracji: ")
    liczbaIteracji= input()
    print("Podaj dokłądność: ")
    dokladnosc= input()
    bisekcja(int(poczatekPrzedzialu),int(koniecPrzedzialu),int(liczbaIteracji),float(dokladnosc))

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