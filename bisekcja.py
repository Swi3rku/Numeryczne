import matplotlib.pyplot as plt
import numpy as np

def bisekcja(przedzialA, przedzialB, liczbaIteracji, dokladnosc,func):
    poczatkowyPrzedzialA = przedzialA
    poczatkowyPrzedzialB = przedzialB
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
    print("Miejsce zerowe: ",round(x,4))
    pom=np.linspace(poczatkowyPrzedzialA,poczatkowyPrzedzialB,100)
    plt.plot(pom,  func(pom),'r')
    plt.plot(pom, 0*pom,'r')
    plt.show()
