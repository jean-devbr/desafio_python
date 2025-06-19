# O mesmo exercício anterior, mas agora, considere que o segundo valor lido poderá ser maior ou menor que o primeiro valor lido, ou seja, deve-se testá-los
try:
    soma = 0
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    if numero2 > numero1:
        print(f'O segundo número "{numero2}" e maior do que o segundo "{numero1}"')
    elif numero1 == numero2:
        print(f'O segundo número "{numero2}" é maior do que o primeiro  número "{numero1}"')
    else:
        print(f'O primeiro número "{numero1}" é maior do que segundo "{numero2}"')
    for i in range(numero1, numero2):
        soma += i
    print(f'A soma entre os números {numero1} e {numero2} é {soma}')
except ValueError:
    print("Erro! Por favor, digite corretamente.")