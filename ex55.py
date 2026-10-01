texto_original = input("Digite uma palavra ou frase:\n")

texto_original = texto_original.lower()
texto_limpo = texto_original.replace(" ", "")


texto_invertido = texto_limpo[::-1]


print(f"\nTexto analisado (sem espaços): {texto_limpo}")
print(f"Texto invertido: {texto_invertido}")

if texto_limpo == texto_invertido:
    print("\nResultado: É um palíndromo!")
else:
    print("\nResultado: Não é um palíndromo.")