
n = int(input("Digite a quantidade de termos (n): "))

if n <= 0:
    print("Por favor, digite um número maior que 0.")
else:
    print(f"Série de Fibonacci até o {n}º termo:") 

    termo1 = 1
    termo2 = 1
    
    for i in range(n):
        print(termo1, end=" ")
        
        proximo = termo1 + termo2
        termo1 = termo2
        termo2 = proximo
        
    print("\n")

