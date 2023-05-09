import math

def f(x):
    return x**2

def g(x):
    return pow(math.e,-x**2)

def zlozenie (x):
    return (x**2) * math.exp(-x**2)

def simpson(f, a, b):
    wynik = ((b-a)/6)*(f(a)+4*f((a+b)/2)+f(b))
    return wynik

def podzielNaPrzedzialy(a,b,liczbaPrzedzialow):
    przedzialy = []
    przesuniecie = (b-a)/liczbaPrzedzialow
    for i in range(liczbaPrzedzialow):
        tmp = (a, a+przesuniecie)
        przedzialy.append(tmp)
        a = a+przesuniecie
    return przedzialy

def newtonCotes(f, a, b, dokladnosc):
    liczbaPrzedzialow = 1
    poprzedniWynik = 0
    wynik = 0
    czyPierwszyRaz = True
    while(abs(poprzedniWynik-wynik)>dokladnosc or czyPierwszyRaz):
        poprzedniWynik = wynik
        wynik = 0
        czyPierwszyRaz = False
        przedzialy = podzielNaPrzedzialy(a,b,liczbaPrzedzialow)
        for i in range(liczbaPrzedzialow):
            wynik += simpson(f,przedzialy[i][0],przedzialy[i][1])
            # print(wynik)
        liczbaPrzedzialow = liczbaPrzedzialow * 2
    return wynik

def gaussHermite(f, n):
    wynik = 0
    if n == 2:
        x, a = [0.88622692, 0.88622692], [-0.70710678, 0.70710678]
    elif n == 3:
        x, a = [0.29540897, 1.18163590, 0.29540897], [-1.22474487, 0.00000000, 1.22474487]
    elif n == 4:
        x, a = [0.08131283, 0.80491409, 0.80491409, 0.08131283], [-1.65068012, -0.52464762, 0.52464762, 1.65068012]
    elif n == 5:
        x, a = [0.01995324, 0.39361932, 0.94530872, 0.39361932, 0.01995324], [-2.02018287, -0.95857246, 0.00000000, 0.95857246, 2.02018287]
    for i in range(n):
        wynik += x[i] * f(a[i])
    return wynik



# print(podzielNaPrzedzialy(0,10,10))
print(newtonCotes(zlozenie, -1, 1, 0.001))
print(gaussHermite(f, 4))
