# Ler 10 valores e escrever quantos desses valores lidos são NEGATIVOS.

contadorNegativo = 0
for i in range(0,10,1):
    valor = float(input(f'Digite o {i +1}° valor: '))
    if valor < 0:
        contadorNegativo += 1
print(f'A quantidade de número negativo é: {contadorNegativo}')


