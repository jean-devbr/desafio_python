#Peça ao usuário para digitar uma nota de 0 a 10 e informe se a nota é:

#Aprovado (7 ou mais)
#Recuperação (4 a 6)
#Reprovado (menos de 4)

nota = int(input("Qual é sua nota? "))

if 0 <= nota < 4:
    print("Você esta REPROVADO")
elif 7<= nota <=10:
    print("Você esta APROVADO")
elif 4 <= nota <= 6:
    print("Você esta de RECUPERAÇÃO")
else:
    print("Erro: Informa uma nota valida entre 0 ate 10!")