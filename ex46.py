numero = int(input("digite o numero da tabuada desejada:\n "))
if (numero<10 and numero>0):

    for i in range(11):
     print(f"{i} x {numero} = {i*numero}")