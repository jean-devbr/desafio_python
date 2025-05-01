#Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos brancos, nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total de eleitores. 

eleitores_municipio = int(input('Digite o total na população que tem no seu município: '))

votos_brancos = int(input('Quantidade de pessoa votaram em branco: '))
if votos_brancos > eleitores_municipio:
    print('Erro! \n Digite um valor menor ou igual da quantidade de pessoa que tem no município')
    while votos_brancos > eleitores_municipio:
        votos_brancos = int(input('Quantidade de pessoa votaram em branco: '))

votos_nulos = int(input('Quantidade de votos em nulos: '))

if votos_brancos == eleitores_municipio:
    print('Erro! Tudo mundo votou em branco')

elif votos_nulos > eleitores_municipio:
    print('Erro! \n Digite um valor menor ou igual da quantidade de pessoa que tem no município')
    while votos_nulos > eleitores_municipio:
        votos_nulos = int(input('Quantidade de votos em nulos: '))


votos_validos = int(input('Quantidade de pessoa que votou válido no seu município: '))

if votos_brancos  == eleitores_municipio or votos_nulos == eleitores_municipio:
    print('Erro! votos em branco ou nulos tem ') 

if votos_validos > eleitores_municipio:
    print('Erro! \n Digite um valor menor ou igual da quantidade de pessoa que tem no município')
    while votos_validos > eleitores_municipio:
        votos_validos = int(input('Quantidade de pessoa que votou válido no seu município: '))

percentual_brancos = (votos_brancos /  eleitores_municipio) * 100 

percentual_nulos = (votos_nulos / eleitores_municipio) * 100

percentual_validos = (votos_validos / eleitores_municipio) * 100

print(f'Quantidade de pessoas que tem no município {eleitores_municipio} \n Quantidade de pessoa que votou em branco {votos_brancos} e o percentual {percentual_brancos:2}% \n Quantidade de pessoas que votou em nulo {votos_nulos} e o percentual {percentual_nulos}% \n Quantidade de pessoas que votou válido {votos_validos} e o percentual {percentual_validos}%')