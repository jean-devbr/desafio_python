#Peça ao usuário para digitar sua idade e informe se ele pode votar ou não. Considere que a idade mínima para votar é 16 anos.

idade = int(input("Informar sua idade: "))

if idade >= 16:
    print("Você já pode votar!")
else:
    print("Você NÂO pode votar!")