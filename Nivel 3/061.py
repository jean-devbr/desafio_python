# Ler 10 valores, calcular e escrever a média aritmética desses valores lidos.
try:
    soma = 0
    for i in range(0,10,1):
        numero = float(input(f'Digite sua {i + 1}° nota: '))
        soma += numero
    media = soma / 10
    print(f'Sua média é {media:.2f}')

except ValueError:
    print("Erro! Por favor, digite apénas números")