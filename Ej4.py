nota_1 = float(input("Primera nota: "))
nota_2 = float(input("Segunda nota: "))
nota_3 = float(input("Tercera nota: "))
examen = float(input("Examen final: "))
trabajo = float(input("Trabajo final: "))

promedio = (nota_1 + nota_2 + nota_3) / 3
nota_final = promedio * 0.40 + examen * 0.50 + trabajo * 0.10 

print("Calificación final:", round(nota_final, 2))