fahrenheit = float()
kelvin = float(0)
graus = float(input("escreva uma temperatura de graus celsius "))

fahrenheit = (graus * 9 / 5) + 32
kelvin = graus + 273.15

print("resultado da conversão /n ")
print(f"\ntemperatura em fahrenheit {fahrenheit}, °f ")
print(f"\ntemperatura em kelvin {kelvin}, k\n ")
