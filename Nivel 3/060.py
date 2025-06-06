# Ler 10 valores e escrever quantos desses valores lidos estão no intervalo [10,20] (inlcuindo os valores 10 e 20 no intervalo) e quantos deles estão fora deste intervalo. 
contador = 0
contadorForaDointervalo = 0
for i in range(0,10,1):
    valor = int(input(f'Digite o {i + 1}° valor: '))
    if valor >= 10 and valor <= 20:
        contador += 1
    else:
        contadorForaDointervalo += 1
print(f'São {contador} valores o intervalo entre 10 a 20. \nSão {contadorForaDointervalo} valores fora do intervalo entre 10 e 20')
    