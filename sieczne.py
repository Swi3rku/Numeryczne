import matplotlib.pyplot as plt
import numpy as np


def sieczne(przedzialA, przedzialB, liczbaIteracji, dokladnosc, func):
    # ===============================================#
    # st -> wyliczanie stycznych                    #
    # dok -> dokładność wyliczenia miejsca zerowego #
    # ===============================================#

    # przypisanie końców przedziału do x
    x = [przedzialA, przedzialB]
    st = przedzialB
    iteracje = 0

    # ===============================================#
    # warunek -> liczba iteracji                     #
    # ===============================================#

    if liczbaIteracji != -1:
        iteracje = liczbaIteracji
        for i in range(0, liczbaIteracji - 1):
            st = x[1] - ((func(x[1]) * (x[1] - x[0])) / (func(x[1]) - func(x[0])))
            # st=round(st,2)
            dok = abs(st - x[1])
            # x[0],x[1]=st,x[0]
            x[0], x[1] = x[1], st

    else:

        # ===============================================#
        # Warunek -> dokładność                          #
        # ===============================================#

        while (True):
            iteracje += 1
            st = x[1] - ((func(x[1]) * (x[1] - x[0])) / (func(x[1]) - func(x[0])))
            dok = abs(st - x[1])
            if (dok < dokladnosc):
                break
            x[0], x[1] = x[1], st

    print("===METODA==SIECZNYCH===")
    print("miejsce zerowe: ", np.format_float_positional(st))
    print("Dokladnosc: ", np.format_float_positional(dok))
    print("Liczba Iteracji: ", iteracje)
    print("=======================")
    pom = np.linspace(przedzialA, przedzialB, 100)
    plt.plot(pom, func(pom), 'r')
    plt.plot(pom, 0 * pom, 'r')
    plt.show()
