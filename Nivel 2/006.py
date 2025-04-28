#Peça ao usuário para digitar dois números e informe qual deles é o maior. Se os números forem iguais, informe que eles são iguais.

n1 = int(input("Inserir um número inteiro: "))
n2 = int(input("Inserir um outro numero inteiro: "))
if n1 > n2:
    print(f'O número {n1} é maior do que {n2}')
elif n1 < n2:
    print(f'O numero {n1} é menor do que {n2}')
else:
    print(f'O número {n1} é igual o número {n2}')