#Escreva um programa que peça ao usuário para digitar um número e informe se ele é par ou ímpar.
num = int(input("digite um numero inteiro: "))
if num % 2 == 0:
    print("Esse número é PAR")
else:
    print("Esse número é IMPAR")