# Uma revendedora de carros usados paga a seus funcionários vendedores um salário fixo por mês, mais uma comissão também fixa para cada carro vendido e mais 5% do valor das vendas por ele efetuadas. Escrever um algoritmo que leia o número de carros por ele vendidos, o valor total de suas vendas, o salário fixo e o valor que ele recebe por carro vendido. Calcule e escreva o salário final do vendedor.

salario_fixo = float(input('Digite seu sálario mensal: '))
numero_de_carro = int(input('Quantidade de carro que você vendeu nesse mês: '))
valor_vendas = float(input('Valor total das vendas: '))
carro_vendido = float(input('Valor que você recebe por carro vendido: '))

comisao_venda_efeituada = valor_vendas * 0.05
comisao_carro_vendido = numero_de_carro * carro_vendido
salario_final = salario_fixo + comisao_carro_vendido + comisao_venda_efeituada
print(f'Seu sálario final é : R$ {salario_final:.2f}')