n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

# Compara os valores e devolve o MENOR deles.
inicio = min(n1, n2) + 1
# Compara os valores e devolve o MAIOR deles.
fim = max(n1, n2)

for num in range(inicio, fim):
    print(num)

