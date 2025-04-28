# Soma de Números
# Peça ao usuário para inserir 10 números e, em seguida, calcule e imprima a soma desses números.

soma = 0

for i  in range(10):
    num = float(input(f'Insira o {i + 1}º número: '))
    soma += num
print(f'A soma dos números inseridos é: {soma}')
