#Crie uma calculadora simples que peça ao usuário para inserir dois números e uma operação (soma, subtração, multiplicação ou divisão). O programa deve realizar a operação e mostrar o resultado. Lembre-se de tratar a divisão por zero.

n1 = int(input("Inserir um numero inteiro: "))
n2 = int(input("Inserir outro numero inteiro: "))
ope = input("Qual é a operação você quer realizar ( soma, subtração, multiplicação ou divisão)? ")

if ope == "soma":
    r = n1 + n2
    print(f'A soma entre {n1} e {n2} é: {r}')
elif ope == "Subtração":
    r = n1 - n2
    print(f'A subtração entre {n1} e {n2} é: {r}')
elif ope == "multiplicação":
    r = n1 * n2
    print(f'A multiplicação entre {n1} e {n2} é: {r}')
elif ope == "divisão":
    if n2 == 0:
        print("Erro: É um resultando indefinido")
    else:
        r = n1 / n2
        print(f'A divisão entre {n1} e {n2} é: {r}')
else:
    print('Operação inválida. Por favor, digite uma operação valida')
