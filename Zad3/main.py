#Jakub(Szymczak + Świerczyński)
import numpy as np
import matplotlib.pyplot as plt
from Zad3.horner import horner


def f(x):
    return x**3


def g(x):
    return np.sin(x) + np.sin(3*x) + np.sin(5*x)


def h(x):
    return horner(x,[1,-3,2], 3)


def funMod(x):
    return abs(abs(x-4)-5)


def notFunLine(x):
    return 3*x-5


def uber(x):
    return h(g(x))
    # return abs(x**2-4*x)+2*x+np.sin(x)+np.cos(2*x)

# oblicza interpolacje na podstawie punktów i zwraca funkcje
def newton_interpolation(x, y):
    n = len(x)
    a = y.copy()  # make a copy of y to avoid modifying the original data
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            a[i] = (a[i] - a[i - 1]) / (x[i] - x[i - j])
    def f(xi):
        result = a[n - 1]
        for i in range(n - 2, -1, -1):
            result = result * (xi - x[i]) + a[i]
        return result
    return f

def wczytaj_z_pliku():
    list = []
    plik = open("wezly", "r", encoding="utf8")
    for wiersz in plik:
        list.append(float(wiersz))
    return list


def wyborFunkcji():
    print("=======================")
    print("Wybierz funkcje:")
    print("1. f(x)=x^3\n"
          "2. g(x)=sin(x) + sin(3x) + sin(5x)\n"
          "3. h(x)=x^2 - 3x + 2\n"
          "4. j(x)=||x-4|-5|\n"
          "5. k(x)=3x-5\n"
          "6. l(x)=h(g(x))\n")
    print("9. Koniec psot")
    print("=======================")
    funkcja = int(input())
    return funkcja

def oblicz_wartosc(wezly, fun):
    wartosci = []
    for i in range(0,len(wezly)):
        # print(i, '\t',round(fun(wezly[i]),4))
        wartosci.append((fun(wezly[i])))
    # print(wartosci)
    return wartosci

# xArgs=[-2,-1,0,1,2]
# yArgs=[-8,-1,0,1,8]
# xArgs2=[-2,2]
# yArgs2=[-8,8]
# x4g=[-2,-1,-0.35,0,1,2]
# y4g=[g(-2),g(-1),g(-0.35),g(0),g(1),g(2)]
# # tworzymy funkcje po interpolacji
# isthisworking=newton_interpolation(x4g, y4g)
# # deklaruje przestrzeń liniową
# pom = np.linspace(-5, 5, 100)
# pom2 = np.linspace(-2, 2, 100)
# # rysuje bazową funkcje
# plt.plot(pom, g(pom), 'r')
# # rysuje funkcje wynikową z interpolacji
# plt.plot(pom2,isthisworking(pom2),'b' ,linestyle="dashed")
# # Rysuje węzły
# plt.scatter(x4g, y4g)
# plt.title('Function with multiple ups and downs')
# plt.show()




wybor = 0
listaFunkcji = [f, g, h, funMod, notFunLine,uber]
while (True):
    wybor = wyborFunkcji()
    if(wybor==9):
        break
    wezly = wczytaj_z_pliku()
    print("\nWczytano wezly:")
    print(wezly)
    obliczoneWart = oblicz_wartosc(wezly, listaFunkcji[wybor-1])
    funKwadrat = newton_interpolation(wezly, obliczoneWart)
    # deklaruje przestrzeń liniową
    maxWezly = max(wezly)
    minWezly = min(wezly)
    pom = np.linspace(minWezly-2, maxWezly+2, 100)
    pom2 = np.linspace(minWezly, maxWezly, 100)
    # rysuje bazową funkcje
    plt.plot(pom, listaFunkcji[wybor-1](pom), 'r')
    # rysuje funkcje wynikową z interpolacji
    plt.plot(pom2,funKwadrat(pom2),'g' ,linestyle="dashed")
    # Rysuje węzły
    plt.scatter(wezly, obliczoneWart)
    if(wybor==2):
        plt.title('Function with multiple ups and downs')
    plt.show()

