num = int(input(("digite um numero inteiro: ")))

fat = 1

for i in range (1, num + 1):
    fat = fat * i

    print(f"o fatorial de {num} é {fat}")
