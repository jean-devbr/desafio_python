# Escreva um algoritmo para ler as notas da 1a. e 2a. avaliações de um aluno, calcule e imprima a média (simples) desse aluno. Só devem ser aceitos valores válidos durante a leitura (0 a 10) para cada nota. 

try:
    nota1 = float(input("Digite sua nota da 1a: "))
    while 0 > nota1  or nota1 > 10:
        nota1 = float(input("Erro! Por favor, digite apenas o número entre 0 a 10. \nDigite novamente sua nota da 1a: "))
    nota2 = float(input("Digite sua nota da 2a: "))
    while 0 > nota2 or nota2 > 10:
        nota2 = float(input("Erro! Por favor,digite apenas o número entre 0 a 10. \nDigite novamente a sua nota da 2a: "))
    media = (nota1 + nota2) / 2
    print(f'Sua média entre as notas {nota1} e {nota2} é: {media:.2f}')

except ValueError:
    print("Erro! Por favor, digite apenas números reais.")