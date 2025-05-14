# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# até 20 litros, desconto de 3% por litro Álcool
# acima de 20 litros, desconto de 5% por litro
# até 20 litros, desconto de 4% por litro Gasolina
# acima de 20 litros, desconto de 6% por litro
# Escreva um algoritmo que leia o número de litros vendidos e o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 3,30 e o preço do litro do álcool é R$ 2,90.

quantidade_em_litros = float(input("Digite a quantidade de litros que você deseja abastecer: "))
while quantidade_em_litros <= 0:
    quantidade_em_litros = float(input("Erro! Por favor, digite um valor maior que 0! \nDigite a quantidade de litros que você deseja abastecer: "))
tipo_de_combustivel = input("Digite [G]-gasolina ou [A]-álcool: ").upper()
while tipo_de_combustivel != "G" and tipo_de_combustivel != "A":
    tipo_de_combustivel = input("Erro! Digite apenas uma letra que esta mandando como A ou G! \nDigite [G]-gasolina ou [A]-álcool: ")

if tipo_de_combustivel == "A":
    valor_por_litro = 2.90
    if quantidade_em_litros <= 20:
        pago_por_cliente = (valor_por_litro * 0.97) * quantidade_em_litros
    else:
        pago_por_cliente = (valor_por_litro * 0.95) * quantidade_em_litros
    
else:
    valor_por_litro = 3.30
    if quantidade_em_litros <= 20:
        pago_por_cliente = (valor_por_litro * 0.96) * quantidade_em_litros
    else:
        pago_por_cliente = (valor_por_litro * 0.94) * quantidade_em_litros

print(f'O valor para ser paga pelo cliente é: R$ {pago_por_cliente:.2f}')    


