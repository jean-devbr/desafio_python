# Escreva um algoritmo para ler 2 valores e se o segundo valor informado for ZERO, deve ser lido um novo valor, ou seja, para o segundo valor não pode ser aceito o valor zero e imprimir o resultado da divisão do primeiro valor lido pelo segundo valor lido. (utilizar a estrutura REPITA).

try:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    while numero2 == 0:
        numero2 = float(input("Erro! Não pode ser zero o segundo número \nDigite novamente o segundo número: "))
        break
    divisao = numero1 / numero2 
    print(f'A divisão entre {numero1} e {numero2} é : {divisao:.2f}')


except ValueError:
    print("Erro! Por favor digite apénas números reais")