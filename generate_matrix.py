def get_index_artificial_variables(lst):
    return [i+1 for i,x in enumerate(lst) if x == 'ge' or x == 'eq']

def count_variables_HE(lst, artificial):
    if artificial:
        return len(lst)-lst.count('le')
    return len(lst)-lst.count('eq')

def get_Binv(A,C):
    ''''Obtengo las A-C ultimas columnas de A'''
    columns_amount=len(A[0])-len(C)
    return [A[i][-columns_amount:] for i in range(len(A))]

def get_Ai_column(A,iColumn):
    return [A[i][iColumn] for i in range(len(A))]

def find_min_and_index(array):
   minimun=min(array)
   index=array.index(minimun)
   return [minimun,index] # [elemento minimo, indice del elemento minimo]

def make_vColumn(iColumn,index):
    divisor=iColumn[index]
    print("Divisor: {}\nColumna {}".format(divisor,iColumn))
    for i in range(len(iColumn)):
        if i == index:
            iColumn[i]=1/divisor
        else:
            iColumn[i]=-iColumn[i]/divisor
    return iColumn

def make_Ematrix(indentiy,vMatrix,index):
    indentiy[index]=vMatrix
    return indentiy

def exists_negativeNumber_in(array):
    return min(array) >= 0