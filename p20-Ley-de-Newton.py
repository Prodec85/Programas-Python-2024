# Calcular la segunda ley de Newton (f = m * a)
import os; os.system("cls")

print("Calcular la segunda ley de Newton (f = m * a)")
print("[ F ] fuerza   f = m * a ")   
print("[ M ] fuerza   m = f / a ")   
print("[ A ] fuerza   a = f / m ")
op = input("Elije la funcion:").upper()

if op == "F":
    print("\nCalculando la Fuerza...")
    m = float(input("Dame la masa."))
    a = float(input("Dame la aceleracion."))
    f = m * a
    print(f"La fuerza es: {f}")

elif op == "M":
    print("\nCalculando la Masa...")
    f = float(input("Dame la fuerza."))
    a = float(input("Dame la aceleracion."))
    m = f / a
    print(f"La masa es: {m}")

elif op == "A":
    print("\nCalculando la Aceleracion...")
    f = float(input("Dame la fuerza."))
    m = float(input("Dame la masa."))
    a = f / m
    print(f"La aceleracion es: {a}")

else:
    print("\nOpcion invalida...")

print("\nProceso terminado...")

