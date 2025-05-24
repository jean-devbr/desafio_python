# Faça um algoritmo para ler as 3 notas obtidas por um aluno nas 3 verificações e a média dos exercícios que fazem parte da avaliação. Calcular a média de aproveitamento, usando a fórmula abaixo e escrever o conceito do aluno de acordo com a tabela de conceitos mais abaixo:
#                        N1 + N2 * 2 + N3 * 3+Média_dos_Exercícios
# Média_de_Aproveitamento =   ----------------------------
#                                   7 
# A atribuição de conceitos obedece a tabela abaixo:
# Média de Aproveitamento Conceito
# > = 9,0                 | A
# > = 7,5 e < 9,0         | B
# > = 6,0 e < 7,5         | C
# < 6,0                   | D 
try:

    nota1 = float(input("Digite sua primeira nota: "))
    while nota1 < 0:
        nota1 = float(input("Erro! Não pode número negativo \nDigite sua primeira nota: "))
    nota2 = float(input("Digite sua segunda nota: "))
    while nota2 < 0:
        nota2 = float(input("Erro! Não pode número negativo \nDigite sua segunda nota: "))
    nota3 = float(input("Digite sua terceira nota: "))
    while nota3 < 0:
        nota3 = float(input("Erro! Não pode número negativo \nDigite sua terceira nota: "))
    mediaExercicio = float(input("Digite sua média de excercício: "))
    mediaAproveitamento = (nota1 + (nota2 * 2) + (nota3 * 3) + mediaExercicio) / 6
    if mediaAproveitamento >= 9:
        conceito = "A"
    elif 7.5 < mediaAproveitamento < 9:
        conceito = "B"
    elif 6 <= mediaAproveitamento < 7.5:
        conceito = "C"
    else:
        conceito = "D"
    print(f'Sua média de aproveitamento é {mediaAproveitamento:.2f} \nO conceito do aluno é {conceito}')
except ValueError:
    print("Erro! Digite um número valor!")