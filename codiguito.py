# =========================================
# CONVERSOR DE MONEDAS - VERSIÓN 3
# Autor(a): NEIL MEZA
# =========================================

soles = float(input("Ingrese la cantidad en soles: "))

print("1. Dólares")
print("2. Euros")
print("3. Libras Esterlinas")

opcion = input("Seleccione una opción: ")

if opcion == "1":
    dolares = soles / 3.60
    print("Equivale a", dolares, "dólares.")

elif opcion == "2":
    euros = soles / 4.20
    print("Equivale a", euros, "euros.")

elif opcion == "3":
    libras = soles / 4.80
    print("Equivale a", libras, "libras.")

else:
    print("Opción no válida.")
