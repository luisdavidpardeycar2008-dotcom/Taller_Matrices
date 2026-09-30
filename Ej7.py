presion = float(input("Ingrese la presión: "))
volumen = float(input("Ingrese el volumen: "))
temperatura = float(input("Ingrese la temperatura: "))

masa = (presion * volumen) / (0.37 * (temperatura + 460))

print("Masa:", masa)