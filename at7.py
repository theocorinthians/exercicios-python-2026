print ("nome da tarefa ")
tarefa = input()

print ("digite nota 1 ")
nota1 = float(input())

print ("digite nota 2 ")
nota2 = float(input())

print ("digite nota 3 ")
nota3 = float(input())

print ("digite nota 4 ")
nota4 = float(input())

calculo = (nota1 + nota2 + nota3 + nota4 ) /4

if (calculo>=7): print ("aprovado")
else:
    print ("reprovado " )

print (f"em  {tarefa}  e sua media final; {calculo}")