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
A = 2
B = 2
C = 4
if (A < B + C) and (B < C + A) and (C < B + A):
    if (A == B) and (C == B):
        print("Triângulo Equilátero")
    elif (A == B) or (A == C) or (B == C):
        print("Triângulo isósceles")
    else:
        print("Triângulo Escaleno")
else:
    print("Não é possível formar um triângulo")