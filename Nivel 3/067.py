# Faça um algoritmo que calcule e escreva a média aritmética dos números inteiros entre 15 (inclusive) e 100 (inclusive). 
soma = 0
contador = 0
for i in range(15,101):
    soma += i
    contador += 1
media = soma / contador
print(media)
