# Acrescentar uma mensagem de 'VALOR INVÁLIDO' no exercício [45] caso o segundo valor informado seja ZERO. 
try:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    while numero2 == 0:
        numero2 = float(input("VALOR INVÁLIDO! Não pode zero. \nDigite novamente o segundo número: "))
        break
    divisao = numero1 / numero2 
    print(f'A divisão entre {numero1} e {numero2} é : {divisao:.2f}')


except ValueError:
    print("Erro! Por favor digite apénas números reais")