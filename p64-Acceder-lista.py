# Acceder a los elementod de una lista de números
import os; os.system("cls")

nums = [10,20,30,40,60,70,10,20,99]

print("Acceder a los elementos de una lista.")
print("La lista                   :", nums)
print("# de elementos de la lista :", len(nums))

print("Acceder con índices positivos 0...8", len(nums))
print("Primero                    :", nums[0])
print("Último                     :", nums[8])
print("Números del 2 al 6         :", nums[2:6])
print("Primeros 3                 :", nums[:3])
print("Úlimos 3                   :", nums[6:])
print("Acceder con índices positivos -9...-1", len(nums))
print("Primero                    :", nums[-9])
print("Último                     :", nums[-1])
print("Números del 2 al 6         :", nums[-7:-3])
print("Primeros 3                 :", nums[:-6])
print("Úlimos 3                   :", nums[-3:])




