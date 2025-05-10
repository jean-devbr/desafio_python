# Ler o salário fixo e o valor das vendas efetuadas pelo vendedor de uma empresa. Sabendo-se que ele recebe uma comissão de 3% sobre o total das vendas até R$ 1.500,00 mais 5% sobre o que ultrapassar este valor, calcular e escrever o seu salário total.

salario_fixo = float(input('Digite seu salário fixo: '))
while salario_fixo < 0:
    salario_fixo = float(input("Erro! Não pode ser salário negativo!\nDigite seu salário fixo: "))
valor_das_vendas = float(input('Digite o valor que você vendeu no mês passado: '))
while valor_das_vendas < 0:
    valor_das_vendas = float(input("Erro! Não pode ser valor negativo!\nDigite o valor que você vendeu no mês passado: "))
if valor_das_vendas <= 1500:
    comisao = valor_das_vendas * 0.03 
else:
    comisao = (1500 * 0.03) + ((valor_das_vendas - 1500) * 0.05)

salario_final = salario_fixo + comisao

print(f'Seu salário final é R$ {salario_final}')