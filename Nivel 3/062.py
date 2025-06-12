# Ler o número de alunos existentes em uma turma e, após isto, ler as notas destes alunos, calcular e escrever a média aritmética dessas notas lidas.

try:
    numeroAluno = int(input("Digite quantos alunos têm na sala de aula: "))
    soma = 0
    for i in range(0,10,1):
        notaCadaAluno = float(input(f'Digite sua nota {i + 1}° : '))
        soma += notaCadaAluno
    media = soma / numeroAluno
    print(f'Média das notas é: {media:.2f}')

except ValueError:
    print("Erro! Por favor, digite apenas número válido.")