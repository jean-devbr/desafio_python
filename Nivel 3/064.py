# Escreva um algoritmo para ler 10 números. Todos os números lidos com valor inferior a 40 devem ser somados. Escreva o valor final da soma efetuada.

try:
    soma = 0
    for i in range(10):
        numero = float(input(f'Digite o {i + 1}° número: '))
        if numero < 40:
            soma += numero
        else:
            print("Esse número não vai ser somado, ok?")
    print(f'A soma dos números é {soma:.2f}')       
except ValueError:
    print("Erro! Por favor, digite apenas números validos") 