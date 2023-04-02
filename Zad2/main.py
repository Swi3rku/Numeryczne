import numpy as np
import sys


def wczytajPlik(nazwaPliku):
    plik = open(nazwaPliku, "r", encoding="utf8")
    i = 0
    for wiersz in plik:
        wierszLista = wiersz.split(' ')
        j = 0
        for liczba in wierszLista:
            a[i][j] = float(liczba)
            j += 1
        i += 1
    # return a


def eliminacjaGaussa(lista, liczbaNiewiadomych):
    for i in range(liczbaNiewiadomych):
        # Find row with largest pivot element and swap with current row
        max_row = i + np.argmax(abs(lista[i:, i]))
        lista[[i, max_row]] = lista[[max_row, i]]
        if (round(lista[i][i], 4) == 0):
            print("znaleziono 0 na przekatnej")
            sys.exit()
        # Eliminate lower triangular part of the matrix
        for j in range(i + 1, n):
            c = lista[j, i] / lista[i, i]
            lista[j, i:] = lista[j, i:] - c * lista[i, i:]


def podstawianieWsteczne(macierz, liczbaNiewiadomych):
    # Making numpy array of n size and initializing
    # to zero for storing solution vector
    wynik = np.zeros(liczbaNiewiadomych)
    # # Back Substitution
    wynik[liczbaNiewiadomych - 1] = macierz[liczbaNiewiadomych - 1][liczbaNiewiadomych] / macierz[liczbaNiewiadomych - 1][liczbaNiewiadomych - 1]

    for i in range(liczbaNiewiadomych - 2, -1, -1):
        wynik[i] = macierz[i][liczbaNiewiadomych]
        for j in range(i + 1, liczbaNiewiadomych):
            wynik[i] = wynik[i] - macierz[i][j] * wynik[j]
        wynik[i] = wynik[i] / macierz[i][i]
    return wynik


n = 0
while (n != -1):
    n = int(input('Podaj liczbe niewiadomych: '))
    fileName = input('Podaj nazwe pliku: ')
    # Making numpy array of n x n+1 size and initializing
    # to zero for storing augmented matrix
    a = np.zeros((n, n + 1))
    wczytajPlik(fileName)
    print('\n', a)
    eliminacjaGaussa(a, n)
    print('\n', a)
    print(podstawianieWsteczne(a, n))
