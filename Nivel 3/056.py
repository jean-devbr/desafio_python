# Ler um valor inteiro (aceitar somente valores entre 1 e 10) e escrever a tabuada de 1 a 10 do valor lido.
try:
    numeroInteiro = int(input("Digite um número inteiro para mostra a tabuada dele de 1 a 10: "))
    while numeroInteiro < 1 or numeroInteiro > 10:
        numeroInteiro = int(input("Erro! Digite apenas números de 1 a 10 \nDigite novamente seu número: "))
    for i in range(1,11):
        print(f'{numeroInteiro} x {i} = {numeroInteiro * i}') 

except ValueError:
    print("Erro! Por favor, digite um número inteiro")