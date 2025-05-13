#Ler dois valores e imprimir uma das três mensagens a seguir:
# ‘Números iguais’, caso os números sejam iguais
# ‘Primeiro é maior’, caso o primeiro seja maior que o segundo;
# ‘Segundo maior’, caso o segundo seja maior que o primeiro.
try:
    numero_1 = float(input("Digite o primeiro número: "))
    numero_2 = float(input("Digite o segundo número: "))

    if numero_1 == numero_2:
        print(f'Os números são iguais {numero_1} e {numero_2}.')
    elif numero_2 > numero_1:
        print(f'O segundo número {numero_2} é maior do que o primeiro número {numero_1}.')
    else:
        print(f'O primeiro número {numero_1} é maior do que o segundo número {numero_2}.')

except ValueError:
    print("Erro! Por favor, digite um número valido.")