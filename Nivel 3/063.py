# Escreva um algoritmo para ler 10 números e ao final da leitura escrever a soma total dos 10 números lidos.
try:
    soma = 0
    for i in range(0,10,1):
        numero = float(input(f'Digite o {i + 1}° número: '))
        soma += numero
    print(f'A soma dos 10 números é {soma:.2f}')

except ValueError:
    print("Erro! Por favor, digite apenas número valido.")