#problema: escreva um software informe a média aritimética de um aluno que cursou 4 bimestres

#Etapas para programar

#1 - obter as 4 notas do aluno
#2 - efetuar a conta
#3 - mostrar a média aritimética

notar1 = int(input("Digite a primeira notar (inteiro): "))
notar2 = int(input("Digite o segunda notar (inteiro): "))
notar3 = int(input("Digite a terceira notar (inteiro): "))
notar4 = int(input("Digite a quarta notar (inteiro): "))

s = (notar1 + notar2 + notar3 + notar4)/4
print(f'A média aritimética dos valores {notar1}, {notar2}, {notar3},{notar4} vale: {s}') #f: serve para fazer uma interpolação de strings
