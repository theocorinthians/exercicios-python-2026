print ("digite lado 1 do triangulo ")
lado1 = int(input())

print ("digite lado 2 do triangulo ")
lado2 = int(input())

print ("digite lado 3 do triangulo ")
lado3 = int(input())

if (lado1 == lado2 and lado1 == lado3):
  print ("equilatero")

elif (lado1 != lado2 and lado1 != lado3 and lado2 != lado3):
    print ("escaleno")

else:
   print ("isoseles")
