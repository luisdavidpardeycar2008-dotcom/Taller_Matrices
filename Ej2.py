sueldo = float(input("Ingrese el sueldo base: "))
venta_1 = float(input("Ingrese la primera venta: "))
venta_2 = float(input("Ingrese la segunda venta: "))
venta_3 = float(input("Ingrese la tercera venta: "))

comision = (venta_1 + venta_2 + venta_3) * 0.10
total = sueldo + comision

print("Comisión:", comision)
print("Total a recibir:", total)