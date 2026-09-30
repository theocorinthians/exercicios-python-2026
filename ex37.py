a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

if(a == 0):
 print("A equação não é do segundo grau igual o theo")

 b = b**2 - (4*a*c)
if(b < 0):
   print("A equação não possui raizes reais porque sim.")

elif(b == 0):
   print("Só possui uma raiz real")

elif(b > 0):
   print("A equação possui duas raizes reais ")