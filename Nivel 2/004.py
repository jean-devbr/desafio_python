#Peça ao usuário para digitar um número de 1 a 7 e informe o dia da semana correspondente (1 para "Domingo", 2 para "Segunda-feira", etc.). Se o número estiver fora desse intervalo, informe que é um número inválido.

dia = int(input("Digite um número de 1 a 7: "))
if dia == 1:
    print("Hoje é domingo")
elif dia == 2:
    print("Hoje é segunda-feira")
elif dia == 3:
    print("Hoje é terça-feira")
elif dia == 4:
    print("Hoje é quarta-feira")
elif dia == 5:
    print("Hoje é quinta-feira")
elif dia == 6:
    print("Hoje é sexta-feira")
elif dia == 7:
    print("Hoje é sabado")
else:
    print(f'Digite um número valido, esse numero {dia} é inválido')
