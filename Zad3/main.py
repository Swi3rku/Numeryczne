import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3
def g(x):
    return  np.sin(x) + np.sin(3*x) + np.sin(5*x)
def l(x):
    return x**2 - 3*x + 2

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
xArgs=[-2,-1,0,1,2]
yArgs=[-8,-1,0,1,8]
xArgs2=[-2,2]
yArgs2=[-8,8]
x4g=[-2,-1,-0.35,0,1,2]
y4g=[g(-2),g(-1),g(-0.35),g(0),g(1),g(2)]
# tworzymy funkcje po interpolacji
isthisworking=newton_interpolation(x4g, y4g)
# deklaruje przestrzeń liniową
pom = np.linspace(-5, 5, 100)
pom2 = np.linspace(-2, 2, 100)
# rysuje bazową funkcje
plt.plot(pom, g(pom), 'r')
# rysuje funkcje wynikową z interpolacji
plt.plot(pom2,isthisworking(pom2),'b' ,linestyle="dashed")
# Rysuje węzły
plt.scatter(x4g, y4g)
plt.title('Function with multiple ups and downs')
plt.show()
