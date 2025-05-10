# Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após, calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito). Também testar se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo', senão escrever a mensagem 'Saldo Negativo'

numero_da_conta = int(input('Digite o número da sua conta: '))
saldo = float(input("Digite seu saldo: "))
debito = float(input("Digite quanto você quer déposita na sua conta: "))
credito = float(input("Digite quanto tem de crédito: "))

saldo_atual = (saldo  - debito) + credito

if saldo_atual >= 0:
    print('--' * 12)
    print(f'Número da conta: {numero_da_conta}\nSeu saldo é positivo {saldo_atual}!')
else:
    print('--' * 12)
    print(f'Número da conta: {numero_da_conta}\nSeu saldo é negativo {saldo_atual}!')