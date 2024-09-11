# Imprimir una tabla de conversion peso a dollar
import os
while(True):
    os.system("cls")
    tc= 19.87
    while(True): #Pide valores hasta que pi < pf
        pi=float(input("Valor de pesos inicial: "))
        pf=float(input("Valor de pesos final:   "))
        if pi< pf:
            break
    c=pi
    print("n\Peso\tDollar")
    print("-"*15)
    while c<= pf:
        print(f"{c}\t{c/tc:.2f}")
        c+=1
    print("-"*15)
    
    if input("Deseas Continualr (S/N)").upper().startswith("N"):break
print("n\Proceso Terminado")