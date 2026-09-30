
intervalo_0_25 = int(0)
intervalo_26_50 = int(0)
intervalo_51_75 = int(0)
intervalo_76_100 = int(0)

num = int(input("Digite o número (negativo para sair):\n"))

while num >= 0:
    if 0 <= num <= 25:
        intervalo_0_25 += 1
    elif 26 <= num <= 50:
        intervalo_26_50 += 1
    elif 51 <= num <= 75:
        intervalo_51_75 += 1
    elif 76 <= num <= 100:
        intervalo_76_100 += 1


print ("total de numero por intervalo ")
print (f"\n O intervalo [0][25] = {intervalo_0_25 } ")
print (f"\n O intervalo [26][50] = {intervalo_26_50 } ")
print (f"\n O intervalo [51][75] = {intervalo_51_75} ")
print (f"\n O intervalo [76][100] = {intervalo_76_100 } ")
