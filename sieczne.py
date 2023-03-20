# import matplotlib.pyplot as plt
# import numpy as np

# def sieczne(przedzialA, przedzialB, liczbaIteracji, dokladnosc, func):
#     #przypisanie końców przedziału do x
#     x=[przedzialA,przedzialB]
#     pr=przedzialA
#     st=przedzialB
#     dok=0
#     iteracje=0
#     #===============================================#
#     # warunek -> liczba iteracji                    #
#     # st -> wyliczanie stycznych                    #
#     # pr -> poprzednia wartość st                   #
#     # dok -> dokładność wyliczenia miejsca zerowego #
#     # poPrzecinku -> ile liczb po przecinku wypisać #
#     #===============================================#
#     if liczbaIteracji != -1:
#         iteracje=liczbaIteracji
#         poPrzecinku=4
#         for i in range(0,liczbaIteracji-1):
#             st=x[1]-((func(x[1])*(x[1]-x[0]))/(func(x[1])-func(x[0])))
#             dok=abs(st-pr)
#             pr=st
#             x[0],x[1]=st,x[0]
#             if(x[0]>x[1]):
#                 x[0],x[1]=x[1],x[0]
#     else:
#         #Warunek -> dokładność
#         ulamek=str(dokladnosc).split('.')[1]
#         poPrzecinku=len(ulamek)
        
#         while(True):
#             iteracje= iteracje + 1
#             st=x[1]-((func(x[1])*(x[1]-x[0]))/(func(x[1])-func(x[0])))
#             dok=abs(st-pr)
#             if(dok<dokladnosc):
#                 break
#             pr=st
#             x[0],x[1]=st,x[0]
#             if(x[0]>x[1]):
#                 x[0],x[1]=x[1],x[0]

#     print("===METODA==SIECZNYCH===")
#     print("miejsce zerowe: ",round(st,poPrzecinku))
#     print("Dokladnosc: ", round(dok,poPrzecinku))
#     print("Liczba Iteracji: ", iteracje)
#     print("=======================")
#     pom=np.linspace(przedzialA,przedzialB,100)
#     plt.plot(pom,  func(pom),'r')
#     plt.plot(pom, 0*pom,'r')
#     plt.show()

import matplotlib.pyplot as plt
import numpy as np

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
            x[0],x[1]=st,x[0]
            
    else:
            #Warunek -> dokładność
        while(True):
               st=x[1]-((func(x[1])*(x[1]-x[0]))/(func(x[1])-func(x[0])))
               if(abs(st-x[1])<dokladnosc):
                   break
               x[0],x[1]=x[1],st

    print("miejsce zerowe: ",st)
    pom=np.linspace(przedzialA,przedzialB,100)
    plt.plot(pom,  func(pom),'r')
    plt.plot(pom, 0*pom,'r')
    plt.show()
