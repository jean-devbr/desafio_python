# Escreva um algoritmo que leia as idades de 2 homens e de 2 mulheres (considere que as idades dos homens serão sempre diferentes entre si, bem como as das mulheres). Calcule e escreva a soma das idades do homem mais velho com a mulher mais nova, e o produto das idades do homem mais novo com a mulher mais velha
homem_primeiro = int(input("Digite uma idade de um homem: "))

homem_segundo = int(input("Digite outra idade de outro homem: "))
while homem_primeiro == homem_segundo:
    homem_segundo = int(input("Erro! Por favor, digite idades diferentes dos homens \nDigite outra idade de outro homem: "))
mulher_primeiro = int(input("Digite uma idade de uma mulher: "))
mulher_segundo = int(input("Digite outra idade de outra mulher: "))
while mulher_primeiro == mulher_segundo:
    mulher_segundo = int(input("Erro! Por favor,digite idades diferentes dos homens \nDigite outra idade de outra mulher: "))

if homem_primeiro > homem_segundo and mulher_primeiro > mulher_segundo:
    soma = homem_primeiro + mulher_segundo
    produto = homem_segundo * mulher_primeiro
else:
    soma = homem_segundo + mulher_primeiro
    produto = homem_primeiro * mulher_segundo

print(f'A soma das idades do homem mais velho e a mulher mais novo é {soma} \nO produto das idades do homem mais novo e a mulher mais velha é {produto}')
