# Acrescente uma mensagem 'NOVO CÁLCULO (S/N)?' ao final do exercício [48]. Se for respondido 'S' deve retornar e executar um novo cálculo, caso contrário deverá encerrar o algoritmo
try:
    nota1 = float(input("Digite sua nota da 1a: "))
    while 0 > nota1  or nota1 > 10:
        nota1 = float(input("Erro! Por favor, digite apenas o número entre 0 a 10. \nDigite novamente sua nota da 1a: "))
    nota2 = float(input("Digite sua nota da 2a: "))
    while 0 > nota2 or nota2 > 10:
        nota2 = float(input("Erro! Por favor,digite apenas o número entre 0 a 10. \nDigite novamente a sua nota da 2a: "))
    while True:
        novoCalculo = input("Novo cálculo S para sim e N para não. Digite S ou N se quer um novo cálculo: ").upper() #Converta para letra maiuscula
        if novoCalculo == "S":
            nota1 = float(input("Digite sua nota da 1a: "))
        while 0 > nota1  or nota1 > 10:
            nota1 = float(input("Erro! Por favor, digite apenas o número entre 0 a 10. \nDigite novamente sua nota da 1a: "))
        nota2 = float(input("Digite sua nota da 2a: "))
        while 0 > nota2 or nota2 > 10:
            nota2 = float(input("Erro! Por favor,digite apenas o número entre 0 a 10. \nDigite novamente a sua nota da 2a: "))
        break #Encerra o loop se a resposta não for 'S'
    media = (nota1 + nota2) / 2
    print(f'Sua média entre as notas {nota1} e {nota2} é: {media:.2f}')

except ValueError:
    print("Erro! Por favor, digite apenas números reais.")