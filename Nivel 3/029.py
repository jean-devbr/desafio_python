# Ler 3 valores (considere que não serão informados valores iguais) e escrever a soma dos 2 maiores. 
try:
    numero_1 = float(input("Digite o primeiro número: "))
    numero_2 = float(input("Digite o segundo número: "))
    while numero_1 == numero_2:
        numero_2 = float(input("Erro! Não pode ser igual!\nDigite o segundo número:"))
    numero_3 = float(input("Digite o terceiro número: "))
    while numero_1 == numero_3 or numero_2 == numero_3:
        numero_3 = float(input("Erro! Não pode ser igual!\nDigite o terceiro número:"))

    
    if (numero_1 < numero_2) and (numero_1 < numero_3):
        soma = numero_2 + numero_3
    elif (numero_2 < numero_1) and (numero_2 < numero_3):
        soma = numero_1 + numero_3
    else:
        soma = numero_1 + numero_2
    print(f'A soma de dois números maiores é {soma}')
except ValueError:
    print("Erro! Digite um número valido")