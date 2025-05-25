"""
inicio 
    ler a, b, c 
    se (a < b+c) e (b <a+c) e (c <a+b) então
        se (a=b) e (b=c) então 
            mens = 'Triângulo Equilátero'
        senão 
            se (a=b) ou (b=c) ou (a=c) então
                mens = 'Triângulo Isósceles' 
            senão
                mens = 'Triângulo Escaleno'
            fim_se 
        fim_se
    senão
        mens = 'Não e possível formar um triângulo'
    fim_se
    escrever mens 
fim 
"""
A = 1
B = 2
C = 3
if (A < B + C) and (B < A + C) and (C < A + B):
    if (A == B) and (C == B):
        print("Triângulo equilátero")
    elif (A == B) or (B == C) or (A == C):
        print("Triângulo isósceles")
    else:
        print("Triângulo escaleno")
else:
    print("Não é possível forma um triângulo")

