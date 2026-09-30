area = float(input("Qual o tamanho em metros quadrados da area a ser pintuda: "))
l = area/3
q = l/18

if (l % 18 > 0):
  q = q + 1
  print(f"A quantidades de latas necessarias é {q: .2f}")
  print(f"O preço total é {80*q: .2f} R$")

else:
  print(f"A quantidade de latas necessarias é {q: .2f}")
  print(f"O preço total é {80*q: .2f} R$")