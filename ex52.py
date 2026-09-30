
n = int(input("Digite um número inteiro n: "))

total_divisoes = 0
print(f"Números primos entre 1 e {n}:")

for i in range(1, n + 1):
    if i == 1:
        eh_primo = False
    else:
        eh_primo = True
        
        
        j = 2
        while j * j <= i:
            total_divisoes += 1
            if i % j == 0:
                eh_primo = False
                break  
            j += 1

 
    if eh_primo:
        print(i, end=" ")

print(f"\nTotal de divisões executadas: {total_divisoes}")