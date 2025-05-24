# Faça um algoritmo para ler: a descrição do produto (nome), a quantidade adquirida e o preço unitário. Calcular e escrever o total (total = quantidade adquirida * preço unitário), o desconto e o total a pagar (total a pagar = total - desconto), sabendo-se que:
# - Se quantidade <= 5 o desconto será de 2%
# - Se quantidade > 5 e quantidade <=10 o desconto será de 3%
# - Se quantidade > 10 o desconto será de 5%

nomeProduto = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade que comprar: "))
precoUnitario = float(input("Digite o preço unitário que você vai pagar: "))

if quantidade <= 5:
    percentualDesconto = 0.02

elif 5 < quantidade <=  10:
    percentualDesconto = 0.03

else:
    percentualDesconto = 0.05

total = quantidade * precoUnitario
desconto = percentualDesconto * total 
totalPagar = total - desconto
print(f'O valor que você ia pagar: R$ {totalPagar:.2f}')

