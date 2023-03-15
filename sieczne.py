import matplotlib.pyplot as plt
import numpy as np
#stare wzorki
#st=(( func(x[0])*x[1] )-( func(x[1])*x[0] ))/(func(x[0])-func(x[1]))
#st=x[0]-( (( func(x[0])*x[1] )-( func(x[1])*x[0] ))/(func(x[0])-func(x[1])) )

def sieczne(przedzialA, przedzialB, liczbaIteracji, dokladnosc, func):
    #przypisanie końców przedziału do x
    x=[przedzialA,przedzialB]
    pr=przedzialA
    st=przedzialB
    #warunek -> liczba iteracji
    if liczbaIteracji != -1:
        for i in range(0,liczbaIteracji-1):
            st=x[1]-((func(x[1])*(x[1]-x[0]))/(func(x[1])-func(x[0])))
            st=round(st,2)
            pr=st
            x[0],x[1]=st,x[0]
            if(x[0]>x[1]):
                x[0],x[1]=x[1],x[0]

    else:
        #Warunek -> dokładność
        while(True):
            st=x[1]-((func(x[1])*(x[1]-x[0]))/(func(x[1])-func(x[0])))
            if(abs(st-pr)<dokladnosc):
                break
            pr=st
            x[0],x[1]=st,x[0]
            if(x[0]>x[1]):
                x[0],x[1]=x[1],x[0]
        

    print("miejsce zerowe: ",st)
    pom=np.linspace(przedzialA,przedzialB,100)
    plt.plot(pom,  func(pom),'r')
    plt.plot(pom, 0*pom,'r')
    plt.show()
