sexo = input("digite seu sexo ")

altura = float(input("digite sua altura "))

if (sexo == "m" or sexo == "h"):

    peso_ideal = (72.2 * altura) - 58
    print (f"seu peso ideal e {peso_ideal} kg ")

elif(sexo == "h" or sexo == "m"):

    peso_ideal = (62.1 * altura) - 44.7
print(f"seu peso ideal e {peso_ideal} kg ")