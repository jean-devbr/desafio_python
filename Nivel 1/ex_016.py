#As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.
print("Digite a quantidade de maça para ser comprada: ")
num_macas = int(input())
desconto = 1.00
normal = 1.80
if num_macas < 12:
    print("você irá pagar pelo valor 1,00")
    custo_total = num_macas * desconto
else:
    print("Você irá pagar pelo valor 1,80")
    custo_total = num_macas * normal

print(f"preço total você irá pagar é: R$ {custo_total:.2f}")
