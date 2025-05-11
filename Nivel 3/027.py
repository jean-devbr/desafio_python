# Ler um valor e escrever se é positivo, negativo ou zero.
try:
    numero = float(input("Digite um número qualquer: "))
    if numero > 0:
        print(f'Esse número {numero} é POSITIVO')
    elif numero == 0:
        print(f'Esse número {numero} é zero')
    else:
        print(f'Esse número {numero} é NEGATIVO')
except ValueError:
    print("Erro! Por favor, digite um número valido")
    
