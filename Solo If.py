nombre1 = input("Ingrese el nombre del producto 1: ")
precio1 = float(input("Ingrese el precio del producto 1: "))

nombre2 = input("Ingrese el nombre del producto 2: ")
precio2 = float(input("Ingrese el precio del producto 2: "))

nombre3 = input("Ingrese el nombre del producto 3: ")
precio3 = float(input("Ingrese el precio del producto 3: "))

total = precio1 + precio2 + precio3

if total < 50000:
    metodo = "Efectivo"
    beneficio = "5% de descuento"
elif total <= 100000:
    metodo = "Tarjeta"
    beneficio = "Sin cambios"
else:
    metodo = "Transferencia"
    beneficio = "2% de cashback"

print("\nResumen de la compra:")
print(f"{nombre1}: ${precio1}")
print(f"{nombre2}: ${precio2}")
print(f"{nombre3}: ${precio3}")
print("Total de la compra:", total)
print("Método recomendado:", metodo)
print("Beneficio:", beneficio)