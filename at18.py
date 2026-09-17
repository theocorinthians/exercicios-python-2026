deposito = float(input("digite o valor do deposito "))
taxa = float(input("digite o valor da taxa "))

rendimento = deposito * (taxa/100)

print (f"/n o valor do rendimento e R$", rendimento )
print (f" o valor depois do rendimento e R$", deposito + rendimento)