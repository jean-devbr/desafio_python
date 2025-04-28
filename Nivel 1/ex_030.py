#Contar quantas vezes um número aparece em um vetor
lista = [11, 11, 223, 0]
n = int(input("Digite um número para contar na ocorrência na lista: "))

contagem = lista.count(n) #count serve para conta quantas vezes um número aparece na lista 
print(f'O número {n} aparece quantas {contagem} vezes na lista: {lista}')