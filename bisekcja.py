import matplotlib.pyplot as plt
import numpy as np

def bisekcja(przedzialA, przedzialB, liczbaIteracji, dokladnosc,func):
    poczatkowyPrzedzialA = przedzialA
    poczatkowyPrzedzialB = przedzialB
    iteracje = 0
    #warunek końca: dokładność
    if(liczbaIteracji==-1):
        x = (przedzialA + przedzialB) / 2
        poprzedniaWartosc = 0
        while(abs(x-poprzedniaWartosc) > dokladnosc):
            dok=abs(x-poprzedniaWartosc)
            iteracje += 1
            if func(x) * func(przedzialA) > 0:
                przedzialA = x
            else:
                przedzialB = x
            poprzedniaWartosc=x
            x = (przedzialA + przedzialB) / 2
    #warunek końca: liczba iteracji
    else:
        iteracje = liczbaIteracji
        pr=0
        for i in range(1, liczbaIteracji):
            x = (przedzialA + przedzialB) / 2
            dok=abs(x-pr)
            if func(x) * func(przedzialA) > 0:
                przedzialA = x
                pr=x
            else:
                przedzialB = x
                pr=x
    print("===METODA===BISEKCJI===")
    print("miejsce zerowe: ",x)
    print("Liczba Iteracji: ", iteracje)
    print("Dokładność: ", dok)
    print("=======================")
    pom=np.linspace(poczatkowyPrzedzialA,poczatkowyPrzedzialB,100)
    plt.plot(pom,  func(pom),'r')
    plt.plot(pom, 0*pom,'r')
    plt.show()
