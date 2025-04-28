# Números Ímpares
# Peça ao usuário para inserir um número e imprima todos os números ímpares de 1 até esse número.
num = int(input('Digite seu número: '))

print(f'Números impares de 1 até {num}')

for i in range(1, num + 1):
    if i % 2 != 0:
        print(i)
