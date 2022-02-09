import numpy as np
from problems import *
from generate_matrix import *
from colorama import init,Fore, Back, Style
from termcolor import colored

init()

def start(A,C,b):
    MAX=float("inf")
    nonBasicVariables_amount=len(A[0])-len(C)
    print("b: {}".format(b))
    Binv=get_Binv(A,C)
    print("Binv {}".format(Binv))
    #indices de las columnas para variables basicas y no basicas
    Cindexes=[x for x in range(len(C))]
    cBindexes=[x for x in range(len(C),len(C)+nonBasicVariables_amount)]
    for _ in range(nonBasicVariables_amount): C.append(0)
    
    cB=np.transpose([[0] for x in range(nonBasicVariables_amount)])
    #Salida del intercambio de variables
    nonBasicVariables=["S{}".format(i) for i in range(1,nonBasicVariables_amount+1)]
    basicVariables=["X{}".format(i) for i in range(1,len(b)+1)]
    print("xB {}".format(nonBasicVariables))
    print("cB {}".format(cB))
    cBBinv=np.dot(cB,Binv)
    print("cBBinv {}".format(cBBinv))
    zi_ci=[]
    Ai=None
    for i in Cindexes:
        #obtengo los valores de la columna i de A
        Ai=get_Ai_column(A,i)
        zi_ci.append(float(np.dot(cBBinv,Ai)-C[i]))
    print("zi-ci {}".format(zi_ci))

    flag=1
    while not exists_negativeNumber_in(zi_ci) and len(zi_ci) != 0:
        minimun=find_min_and_index(zi_ci)
        print("Minimo {}".format(minimun))
        print(colored("Entra {}".format(basicVariables[minimun[1]]),'green'))
        
        t=np.dot(Binv,get_Ai_column(A,minimun[1])).tolist() 
        print("T{} {}".format(flag,t))
        right_side=np.dot(Binv,b).tolist()
        print("Lado derecho {}".format(right_side))
        #realizo la division LadoDerechoi/Ti
        divisions=[]
        for i in range(len(t)):
            try:
                if t[i] <= 0: divisions.append(MAX)
                else: divisions.append(float(right_side[i]/t[i]))
            except ZeroDivisionError:
                print("division en lado derecho")
                divisions.append(MAX)
        min_rightSide_Ti=find_min_and_index(divisions)
        print("Minimo LDerecho/Cpivote {}".format(min_rightSide_Ti))

        print(colored("Sale {}".format(nonBasicVariables[min_rightSide_Ti[1]]),'red'))

        v=make_vColumn(t,min_rightSide_Ti[1])
        print("V {}".format(v))
        E=np.transpose(make_Ematrix(np.identity(len(Binv)),v,min_rightSide_Ti[1]))
        print("E {}".format(E))
        input('*'*8+'Fin de la iteracion {}'.format(flag)+'*'*8)
        #calculo el nuevo Binv
        Binv=np.dot(E,Binv)
        cB[0][min_rightSide_Ti[1]]=C[minimun[1]]
        
        Cindexes[minimun[1]]=cBindexes[min_rightSide_Ti[1]]
        
        nonBasicVariables[min_rightSide_Ti[1]]=basicVariables[minimun[1]]
        
        print("Nueva Binv\n {}".format(Binv))
        
        print("Nuevo cB {}".format(cB))
        cBBinv=np.dot(cB,Binv)
        print("Nuevo cBBinv {}".format(cBBinv))
        print("xB {}".format(nonBasicVariables))

        zi_ci=[]
        Ai=None
        for i in Cindexes:
            #obtengo los valores de la columna i de A
            Ai=get_Ai_column(A,i)
            zi_ci.append(float(np.dot(cBBinv,Ai))-C[i])
        print("zi-ci {}".format(zi_ci))
        flag+=1

    # salgo del bucle para imprimir el final
    print("*"*8+" Resultado final "+"*"*8)
    optimal_rightSide=np.dot(Binv,b)
    print(Back.GREEN+"Lado derecho optimo: {}".format(optimal_rightSide))
    optimal_Z=np.dot(cB,optimal_rightSide)
    print(Back.GREEN+"Z optima {}".format(optimal_Z))


start(problem1["A"],problem1["C"],problem1["b"])
