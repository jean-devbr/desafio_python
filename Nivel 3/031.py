# Ler 3 valores (A, B e C) representando as medidas dos lados de um triângulo e escrever se formam ou não um triângulo. OBS: para formar um triângulo, o valor de cada lado deve ser menor que a soma dos outros 2 lados.
A = float(input("Digite o primemeiro lado de um triângulo: "))
B = float(input("Digite o segundo lado de um triângulo: "))
C = float(input("Digite o terceiro lado de um triângulo: "))

if A < B + C:
    if B < A + C:
        if C < B + A:
            print(f'Valores de {A:.2f}, {B:.2f} e {C:.2f} pode forma um triângulo.')
else:
    print(f' Valores de {A:.2f}, {B:.2f} e {C:.2f} NÃO pode forma um triângulo.')