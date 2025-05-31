# Modifique o exercício anterior para aceitar somente valores maiores que 0 para N. Caso o valor informado (para N) não seja maior que 0, deverá ser lido um novo valor para N. 
try:
    N = int(input("Digite um valor maior do que zero: "))
    while N <= 0:
        N = int(input("Erro! Digite um apena um valor positivo e maior do que zero! \nDigite novamente um valor maior do que zero"))
    for i in range(1, N + 1, 1):
        print(i)

except ValueError:
    print("Erro! Digite um número valido")