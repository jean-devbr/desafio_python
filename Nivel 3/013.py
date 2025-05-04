# Faça um algoritmo que leia três notas de um aluno, calcule e escreva a média final deste aluno. Considerar que a média é ponderada e que o peso das notas é 2, 3 e 5. Fórmula para o cálculo da média final é:
#                   n1 * 2 + n2 * 3 + n3 * 5
# mediafinal = -----------------------------------
#                              10
print('Em baixo você vai digita as três notas sua de 0 a 10!')
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
nota3 = float(input('Digite a sua terceira nota: '))

media_final = ((nota1 * 2) + (nota2 * 3 ) + (nota3 * 5)) / 10
print(f'Sua média final é: {media_final:.2f}')