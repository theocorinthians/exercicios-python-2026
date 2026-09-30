
v1 = 0
v2 = 0
v3 = 0


el = int(input("Quantos eleitores tem \n\n"))


for i in range(1, el + 1):
    print("\n Escolha seu voto \n")
    print(" Candidato A - 1 ")
    print(" Candidato B - 2 ")
    print(" Candidato C - 3 \n")
    
    votos = int(input("Digite o número do candidato: "))
    

    if votos == 1:
        v1 += 1
    elif votos == 2:
        v2 += 1
    elif votos == 3:
        v3 += 1

print(f"\nCandidato 1 \n{v1}\nCandidato 2 \n{v2}\nCandidato 3 \n{v3}")