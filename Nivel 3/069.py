# O mesmo exercício anterior, mas agora não será informado o número de mercadorias em estoque. Então o funcionamento deverá ser da seguinte forma: ler o valor da mercadoria e perguntar ‘MAIS MERCADORIAS (S/N)?’. Ao final, imprimir o valor total em estoque e a média de valor das mercadorias em estoque. 
try:
    estoque = 1562
    valorCadaMercadoria = 6
    print(f'Você tem {estoque} estoque')
    temEstoque = input("Você quer mais mercadorias? \n" \
                       "Digite [S] para SIM ou [N] para não: "
                       ).upper()
    if temEstoque == "S":
        valor = estoque * valorCadaMercadoria
    elif temEstoque == "N":
        print("Você encerrou!")
    else:
        print("Erro!")
    media = valor / estoque
    print(
        f'Valor total do estoque R$ {valor:.2f} \n'
        f'A média do valor das mercadorias é {media:.2f}'
        )
except ValueError:
    print("Erro! Digite corretamente")