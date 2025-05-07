# Ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.
print('A seguir vou pedi para você digita dois números diferentes entre si!')
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
while n2 == n1:
    print(f'Os números {n2} e {n1} são iguais! ELes devem ser diferentes!')
    n2 = float(input('Digite novemente (segundo número): '))
if n1 > n2:
    print(f'A ordem crescente é {n2} e {n1}')

else:
    print(f'A ordem crescente é {n1} e {n2}')