#Imprime números de 100 a 1 en decrementos de 1 usando for

import os; os.system("cls")

""" print(list(range(1,10,1)))
print(list(range(1,10,2)))
print(list(range(1,10,3)))
print(list(range(10,0,-1))) """

n = int(input("Desde donde desas descender ?"))


for x in range(n,0,-1):
    print(x, end=" ")