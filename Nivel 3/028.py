# Ler 3 valores (considere que não serão informados valores iguais) e escrever o maior deles. 
try:
    numero_1 = float(input("Digite o primeiro número: "))
    numero_2 = float(input("Digite segundo número: "))
    while numero_1 == numero_2:
        print('Erro! Não pode ser números iguais')
        numero_2 = float(input("Digite segundo número: "))
    numero_3 = float(input("Digite o terceiro número: "))
    while numero_1 == numero_3 or numero_2 == numero_3:
        print('Erro! Não pode ser números iguais')
        numero_3 = float(input("Digite o terceiro número: "))
    maior_numero = max(numero_1, numero_2, numero_3)
    print(f'O maior número é: {maior_numero}')
except ValueError:
    print('Erro! Por favor, digite números validos!')
