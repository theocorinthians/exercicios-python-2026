import math

coe1 = float(input("digite o primeiro coeficiente "))
coe2 = float(input("digite o segundo coeficiente "))
coe3 = float(input("digite o terceiro coeficiente "))

if (coe1 == 0):
    print("o primeiro coeficiente não pode ser 0. ")
else:
    delta = (coe2 ** 2) - (4 * coe1 * coe3)
    print(f"o valor de delta é {delta}")

if (delta > 0):
    x = (-coe2 + math.sqrt(delta)) / (2 * coe1)
    z = (-coe2 - math.sqrt(delta)) / (2 * coe1)
    print(f"x = {x} ")
    print (f"z = {z}")

elif (delta == 0):
    x = -coe2 / (2 * coe1)
    print (f"x = z = {x}")
else:
    print ("equação invalida")