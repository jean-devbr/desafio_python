#Peça ao usuário para digitar os comprimentos de três lados e determine se é possível formar um triângulo. Lembre-se da regra: a soma de dois lados deve ser sempre maior que o terceiro lado.

a = int(input("Inserir um lado do triângulo: "))
b = int(input("Inserir segundo lado do triângulo: "))
c = int(input(("Inserir terceiro lado do triângulo: ")))

if b-c < a < b + c:
    print(f'Os lados do triângulo {a}, {b} e {c}, forma um triângulo')
else:
    print(f'Os lados do triângulo {a}, {b} e {c}, NÃO forma um triângulo')