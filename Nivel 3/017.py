# Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples e escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que nota igual ou maior que 6 o aluno é aprovado). Escrever também a média calculada.

nota1 = float(input('Sua nota da 1a é: '))
nota2 = float(input('Sua nota da 2a é: '))
media = (nota1 + nota2) / 2 
if media >= 6:
    print(f'Você foi APROVADO!Sua média é {media:.2f}')
else:
    print(f'Você foi REPROVADO!Sua média é {media:.2f}')