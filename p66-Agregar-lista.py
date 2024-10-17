# Agregar elementos a una lista de números

import os; os.system("cls")

nums=[80.3,12.5,60.2,30.4]
print("Agregar elementos a una lista de números")

print("Los números: ", nums, len(nums))

print("Agregar 2 elementos adicionales")
nums.append(90)
nums.append(100)

print("Los números: ", nums, len(nums))

print("Insertar elemento en la posición 1")
nums.insert(1,85.5)
print("Queda : ", nums, len(nums))

print("Insertar un rango de elementos")
nums.extend([110,120,130])
print("Queda : ", nums, len(nums))

