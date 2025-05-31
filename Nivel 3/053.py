# ler um valor N e imprimir todos os valores inteiros entre 1 (inclusive) e N (inclusive). Considere que o N será sempre maior que ZERO
N = int(input("Digite um valor maior do que 0: "))
for i in range(1, N + 1, 1):
    print(i)