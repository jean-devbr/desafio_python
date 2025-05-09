#Para o enunciado a seguir foi elaborado um algoritmo em Português Estruturado que contém erros, identifique os erros no algoritmo apresentado abaixo:
# Enunciado: Tendo como dados de entrada o nome, a altura e o sexo (M ou F) de uma pessoa, calcule e mostre seu peso ideal, utilizando as seguintes fórmulas:
# - para sexo masculino: peso ideal = (72.7 * altura) - 58
# - para sexo feminino: peso ideal = (62.1 * altura) - 44.7
# inicio
#ler nome
#ler sexo
#se sexo = M então
    #peso_ideal  (72.7 * altura) - 58
#senão
#   peso_ideal  (62.1 * altura) – 44.7
#fim_se
#escrever peso_ideal
#fim 

nome = input('Digite seu nome: ')
sexo = input('Qual é seu sexo. Para masculino [M] ou Feminino [F]: ') .upper # converte para letra maiúsculas
while sexo != "F" and sexo != "M":
    print(f'Erro: Por favor insira apenas F ou M')
    sexo = input('Qual é seu sexo. Para masculino [M] ou Feminino [F]: ')
altura = float(input('Digite seu altura em metros: '))
if sexo == "M":
    peso_ideal = (72.7 * altura) - 58
else:
    peso_ideal = (62.1 * altura) - 44.70

print(f'Seu nome é {nome}, seu sexo é {sexo} e seu peso ideal é {peso_ideal:.2f} kg')