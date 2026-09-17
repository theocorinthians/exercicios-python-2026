base = float(input("Base (> 0): "))
while base <= 0:
    base = float(input("Erro! Digite a base maior que zero: "))

expoente = float(input("Expoente (> 0 e <= 10): "))
while expoente <= 0 or expoente > 10:
    expoente = float(input("Erro! Expoente deve ser entre 0 e 10: "))

print(f"Resultado: {base ** expoente}")
