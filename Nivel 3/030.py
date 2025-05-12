#Ler 3 valores (considere que não serão informados valores iguais) e escrevê-los em ordem crescente.

try:
    numero_1 = float(input("Digite o primeiro número: "))
    numero_2 = float(input("Digite o segundo número: "))
    while numero_1 == numero_2:
        numero_2 = float(input("Erro! Números iguais!\nDigite o segundo número: "))
    numero_3 = float(input("Digite o terceiro número: "))
    while numero_1 == numero_3 or numero_2 == numero_3:
        numero_3 = float(input("Erro! Números iguais!\nDigite o terceiro número: "))
    if (numero_1 > numero_2) and ( numero_1 > numero_3) and (numero_2 > numero_3):
        ordem = numero_3, numero_2, numero_1
    elif (numero_1 > numero_2) and (numero_1 > numero_3) and (numero_2 < numero_3):
        ordem = numero_2, numero_3, numero_1
    elif (numero_2 > numero_1) and (numero_2 > numero_3) and (numero_3 < numero_1):
        ordem = numero_2, numero_1, numero_3
    elif (numero_2 > numero_1) and (numero_2 > numero_3) and (numero_3 > numero_1):
        ordem = numero_1, numero_3, numero_2
    elif (numero_3 > numero_1) and (numero_3 > numero_2) and (numero_2 > numero_1):
        ordem = numero_1, numero_2, numero_3
    else:
        ordem = numero_2, numero_1, numero_3
    print(f'A ordem é {ordem[0]:.2f}, {ordem[1]:.2f} e {ordem[2]:.2f}')

except ValueError:
    print("Erro! Digite um número valido")