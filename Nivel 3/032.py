#Ler o nome de 2 times e o número de gols marcados na partida (para cada time). Escrever o nome do vencedor. Caso não haja vencedor deverá ser impressa a palavra EMPATE.

primeiro_time = input("Digite o primeiro time que esta jogando: ")
gol_primeimro_time = int(input("Digite quanto gol(s) o primeiro time fez: "))
while gol_primeimro_time < 0:
    gol_primeimro_time = int(input('Erro! Digite um valor positivo (acima de 0).\nDigite quanto gol(s)o primeiro time fez: '))
segundo_time = input("Digite o segundo time que esta jogando: ")
gol_segundo_time = int(input("Digite quanto gol(s) o segundo time fez: "))
while gol_segundo_time < 0:
    gol_segundo_time = int(input('Erro! Digite um valor positivo (acima de 0).\nDigite quantos gol(s) o segundo time fez: '))
if gol_primeimro_time > gol_segundo_time:
    print(f'O {primeiro_time} ganhou de {gol_primeimro_time} a {gol_segundo_time}.')
elif gol_segundo_time > gol_primeimro_time:
    print(f'O {segundo_time} ganhou de {gol_segundo_time} a {gol_primeimro_time}.')
else:
    print(f'Ambos times ({primeiro_time} x {segundo_time}) empataram de {gol_primeimro_time} a {gol_segundo_time}')