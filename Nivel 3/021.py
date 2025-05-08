 # Ler a hora de início e a hora de fim de um jogo de Xadrez (considere apenas horas inteiras, sem os minutos) e calcule a duração do jogo em horas, sabendo-se que o tempo máximo de duração do jogo é de 24 horas e que o jogo pode iniciar em um dia e terminar no dia seguinte.

inicio = int(input('Digite a hora que começou o jogo (entre 1 e 24): '))
while inicio < 1 or inicio > 24:
    print(f'Erro! O tempo deve estar entre 1 e 24!')
    inicio = int(input('Digite a hora que começou o jogo: '))

termino = int(input('Digite a hora que terminou o jogo (entre 1 e 24): '))
while termino < 1 or termino > 24:
    print(f'Erro! O tempo deve estar entre 1 e 24!')
    termino = int(input('Digie a hora que terminou o jogo: '))


if inicio > termino:
    tempo = (24 - inicio) + termino
else:
    tempo = termino - inicio

print(f'A duranção do jogo foi {tempo} horas')