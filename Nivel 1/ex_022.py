# Contagem regressiva de 10 a 1
r = int(input("Contagem regressiva de 10 até 1: "))
if 1 <= r <= 10:
    print("Esta chegando...")
    for i in range(10, 0, -1):
        print(i)
    print("fogo")
else:
    print("Erro: digite o número entre 1 até 10!")
