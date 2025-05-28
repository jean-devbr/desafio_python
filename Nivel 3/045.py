# Reescreva o exercício anterior utilizando a estrutura ENQUANTO. 

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