num = int(input("Digite um numero menor que 1000: "))

if(num<=1000):
   cen = num/100
   dez = (num//10) % 10
   un = num%10
print(f"O numero {num} tem {cen: .0f} centenas")
print(f"O numero {num} tem {dez: .0f} dezenas")
print(f"O numero {num} tem {un: .0f} unidades")