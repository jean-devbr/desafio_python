# As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.
maca = int(input('Quantidade de maças você quer: '))
if maca < 12:
    preco = maca * 1.30
    print(f'Você vai pagar pelo valor: R$ {preco:.2f}')
else:
    preco = maca * 1
    print(f'Você vai pagar pelo valor: R$ {preco:.2f}')