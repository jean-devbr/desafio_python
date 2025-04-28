# Média de Notas
# Peça ao usuário para inserir 5 notas de alunos e calcule a média. Imprima a média e uma mensagem indicando se o aluno foi aprovado (média >= 7) ou reprovado.

for i in range(5):
    nota = int(input(f'Sua {i + 1}º nota é: '))
    nota += i

print(nota)