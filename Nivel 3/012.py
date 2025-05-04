# Escreva um algoritmo para ler uma temperatura em graus Fahrenheit, calcular e escrever o valor correspondente em graus Celsius (baseado na fórmula abaixo):
#     C           F -  32
# ---------- = -----------
#      5             9 
# Observação: Para testar se a sua resposta está correta saiba que 100°C = 212F 

Fahrenheit = int(input('Qual é a temperatura em fehrenheit: '))
converte_para_celsius = ((Fahrenheit - 32) / 9 ) * 5
print(f'Temperatura em {Fahrenheit}, consertendo para Fahrenheit é {converte_para_celsius:.2f}')