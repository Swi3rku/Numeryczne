#Jakub(Szymczak + Świerczyński)
import numpy as np


def wczytajPlik(nazwaPliku, lista):
    plik = open(nazwaPliku, "r", encoding="utf8")
    i = 0
    for wiersz in plik:
        wierszLista = wiersz.split(' ')
        j = 0
        for liczba in wierszLista:
            lista[i][j] = float(liczba)
            j += 1
        i += 1
    return lista


def zaokr(lista):
    eps=1e-8
    mask = np.isclose(lista,0,atol=eps)
    lista[mask] = 0.0


def eliminacjaGaussa(lista, liczbaNiewiadomych):
    for i in range(liczbaNiewiadomych):
        # Element glowny
        max_row = i + np.argmax(abs(lista[i:, i]))
        lista[[i, max_row]] = lista[[max_row, i]]
        # postac trojkatna
        for j in range(i + 1, n):
            c = lista[j, i] / lista[i, i]
            lista[j, i:] = lista[j, i:] - c * lista[i, i:]
    zaokr(lista)
    print(lista)
    if(lista[len(lista)-1][len(lista)-1]==0 and lista[len(lista)-1][len(lista)]==0):
        print("Układ nieoznaczony")
        return -1
    if(lista[len(lista)-1][len(lista)-1]==0 and lista[len(lista)-1][len(lista)]!=0):
        print("Układ sprzeczny")
        return -1
    return 0


def podstawianieWsteczne(macierz, liczbaNiewiadomych):
    wynik = np.zeros(liczbaNiewiadomych)
    wynik[liczbaNiewiadomych - 1] = macierz[liczbaNiewiadomych - 1][liczbaNiewiadomych] / macierz[liczbaNiewiadomych - 1][liczbaNiewiadomych - 1]
    for i in range(liczbaNiewiadomych - 2, -1, -1):
        wynik[i] = macierz[i][liczbaNiewiadomych]
        for j in range(i + 1, liczbaNiewiadomych):
            wynik[i] = wynik[i] - macierz[i][j] * wynik[j]
        wynik[i] = wynik[i] / macierz[i][i]
    return wynik



n = 0
while (True):
    print("Zakoncz program: -1")
    n = int(input('Podaj liczbe niewiadomych: '))
    if(n==-1):
        break
    fileName = input('\nPodaj nazwe pliku: ')
    macierz = np.zeros((n, n + 1))
    macierz = wczytajPlik(fileName,macierz)
    print("\nWczytano macierz:")
    print(macierz, '\n')
    if(eliminacjaGaussa(macierz, n) == 0):
        print(podstawianieWsteczne(macierz, n))
