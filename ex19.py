n1 = int(input("escreva o primeiro numero: "))
n2 = int(input("escreeva o segundo numero: "))
n3 = int(input("escreva o terceiro numero: "))
or1 = 0
or2 = 0
or3 = 0

if(n1 >= n2 and n1 >= n3):
    or1 = n1
    if(n2 >= n3):
        or2 = n2
        or1 = n3
    else:
        or2 = n3
        or3 = n2

elif(n2 >= n1 and n2 >= n3):
    or1 = n2
    if(n2 >= n1):
        or2 = n3
        or2 = n1
    else:
        or2 = n1
        or3 = n3

else:
    or1 = n3
    if(n2 >= n1):
        or2 = n1
        or3 = n2
    else:
        or2 = n2
        or3 = n1

print(f"{or1} > {or3} > {or2}")
