# Cálculo de remuneración, pidiendo al usuario cantidad de horas y valor de la hora.
hours1 = float(input('Hours: '))
rate = float(input('Rate: '))
# Si la cantidad de horas está por encima de 40, calcular sobre el excedente un x1.5 del valor de la hora.
if hours1 > 40:
    hours2 = 40+(hours1-40)*1.5
else:
    hours2 = hours1
print(hours2*rate)
