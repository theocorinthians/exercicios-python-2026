nota = 999
while nota < 0 or nota > 10:
  nota = float(input("escreva uma nota entre 0 e 10: "))
  if(nota < 0 or nota > 10):
    print("nota invalida ")