# Ler dois valores (considere que não serão lidos valores iguais) e escrever o maior deles.

print('Digite dois números diferentes entre si!')
n1 = float(input('Digite primeiro número: ')) 
n2 = float(input('Digite segundo número: '))
while n1 == n2:
    print(f'Número {n2} são iguais {n1}.Eles devem ser diferentes!')
    n2 = float(input('Digite novamente: '))
if n1 > n2:
    print(f'Número {n1} é MAIOR que o número {n2}')

else:
    print(f'Número {n2} é MAIOR que o número {n1}')