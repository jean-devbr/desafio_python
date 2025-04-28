#Escreva um algoritmo para ler as dimensões de um retângulo (base e altura), calcular e escrever a área do retângulo
try: #serve para controla o erro do usuário se  não escrever corretamente 
    m = "metro(s)"
    base = float(input(f"Digite um valor qualquer do comprimento da base do retângulo {m}: "))
    altura = float(input(f"Digite um outro valor qualquer da alturar do retângulo {m}: "))
    area = base * altura
    print("Sua área é:",area)
except ValueError: #mostrar a mensagem do erro entre as aspas
    print("Por favor, insira um número valido.")
