n1 = int(input("Digite primeiro numero: "))
n2 = int(input("Digite segundo numero: "))
n3 = int(input("Digite terceiro numero: "))
n4 = int(input("Digite quarto numero: "))
n5 = int(input("Digite quinto numero: "))

if (n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5):
    print(f"o maior numero é {n1}")
elif (n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5):
    print(f"o maior numero é {n2}")
elif (n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5):
    print(f"o maior numero é {n3}")
elif (n4 > n1 and n4 > n3 and n4 > n2 and n4 > n5):
    print(f"o maior numero é {n2}")
else:
    print(f"maior numero {n5}")

