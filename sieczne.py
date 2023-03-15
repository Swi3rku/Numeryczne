import matplotlib.pyplot as plt
import numpy as np

def sieczne(przedzialA, przedzialB, liczbaIteracji, dokladnosc, func):
    #przypisanie końców przedziału do x
    x=[przedzialA,przedzialB]
    pr=przedzialA
    # wzór do liczenia stycznych
    for i in range(0,liczbaIteracji-1):
        st=(( func(x[0])*x[1] )-( func(x[1])*x[0] ))/(func(x[0])-func(x[1]))
        #st=x[0]-( (( func(x[0])*x[1] )-( func(x[1])*x[0] ))/(func(x[0])-func(x[1])) )
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
