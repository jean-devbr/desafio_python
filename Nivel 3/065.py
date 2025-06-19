# Ler 2 valores, calcular e escrever a soma dos inteiros existentes entre os 2 valores lidos (incluindo os valores lidos na soma). Considere que o segundo valor lido será sempre maior que o primeiro valor lido.

try:
    soma = 0
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    while numero2 <= numero1:
        numero2 =int(input("Erro! o segundo número tem que ser maior do que o primeiro \nDigite novamente o segundo número: "))
    for i in range(numero1, numero2 + 1):
        soma += i
    
    print(f"A soma dos inteiros entre {numero1} e {numero2} é: {soma}")
except ValueError:
    print("Erro! Por favor, digite corretamente.")