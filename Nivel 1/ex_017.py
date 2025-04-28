 #Ler 3 valores (considere que não serão informados valores iguais) e escrever o maior deles.

#etapas para resolver:
	#1 - peça os 3 valores
	#2 - descobrir e mostrar o maior

n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))
n3 = int(input("Informe o terceiro número: "))

if n1 > n2 and n1 > n3:
    print("O primeiro é maior")
elif n2 > n1 and n2 > n3:
    print("O segundo é maior")
else:
    print("O terceiro é maior")
--------------
n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))
while n2 == n1:
    n2 = int(input("informe novamente"))
n3 = int(input("Informe o terceiro número: "))

if n1 > n2 and n1 > n3:
    print("O primeiro é maior")
elif n2 > n1 and n2 > n3:
    print("O segundo é maior")
else:
    print("O terceiro é maior")
