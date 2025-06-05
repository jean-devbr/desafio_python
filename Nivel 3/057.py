#Reescreva o exercício 50 utilizando a estrutura REPITA e um CONTADOR
while True:
    numeroInteiro = int(input("Digite o número 1 para começa a contagem: "))
    if numeroInteiro == 1:
        break
    else:
        print("Erro! É apenas número 1. Digite novamente")

contador = 1
while contador <= 10:
    print(contador)
    contador += 1

print("Fim")