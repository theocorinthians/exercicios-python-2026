while True:
    numero = float(input("Digite um número positivo e maior que zero: "))

    if numero > 0:
        break
    else:
       print("Número inválido! O número deve ser maior que zero.\n") 

quadrado = numero ** 2
cubo = numero ** 3
raiz_quadrada = numero ** 0.5

print("\n Resultados ")
print(f"Número digitado: {numero}")
print(f"O número ao quadrado é: {quadrado}")
print(f"O número ao cubo é: {cubo}")
print(f"A raiz quadrada do número é: {raiz_quadrada}")
