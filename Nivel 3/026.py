# Faça um algoritmo para ler: quantidade atual em estoque, quantidade máxima em estoque e quantidade mínima em estoque de um produto. Calcular e escrever a quantidade média ((quantidade média = quantidade máxima + quantidade mínima)/2). Se a quantidade em estoque for maior ou igual a quantidade média escrever a mensagem 'Não efetuar compra', senão escrever a mensagem 'Efetuar compra'. 

quantidade_atual = int(input("Digite a quantidade atual do seu estoque para um produto: "))
while quantidade_atual < 0:
    print('Erro! Não pode ser negativo!')
    quantidade_atual = int(input("Digite a quantidade atual do seu estoque para um produto: "))
quantidade_maxima = int(input('Digite qunatidade maximo para um produto: '))
while quantidade_maxima < 0:
    print('Erro! Não pode ser negativo!')
    quantidade_maxima = int(input('Digite qunatidade maximo para um produto: '))
quantidade_minima = int(input('Digite a quantidade mínima para um produto: '))
while quantidade_minima < 0:
    print('Erro! Não pode ser negativo!')
    quantidade_minima = int(input('Digite a quantidade mínima para um produto: '))

quantidade_media = (quantidade_maxima + quantidade_minima) / 2

if quantidade_atual > quantidade_media:
    print('-' * 12)
    print(f'Não efetuar a compra.\nA quantidade atual é ({quantidade_atual}) maior do que a média {quantidade_media}')
elif quantidade_atual == quantidade_media:
    print('-' * 12)
    print(f'Não efetuar a comprar.\nA quantidade atual é {quantidade_atual} e {quantidade_media} são ambas iguais!')
else:
    print('-' * 12)
    print(f'Efetuer a compra.\nA quantidade atual é ({quantidade_atual}) menor do que a média {quantidade_media}')