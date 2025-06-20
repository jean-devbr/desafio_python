# Uma loja está levantando o valor total de todas as mercadorias em estoque. Escreva um algoritmo que permita a entrada das seguintes informações: a) o número total de mercadorias no estoque; b) o valor de cada mercadoria. Ao final imprimir o valor total em estoque e a média de valor das mercadorias. 

try:
    totalMercadorias = int(input("Digite o total da mercadoria que tem no estoque: "))
    while totalMercadorias <= 0:
        totalMercadorias = int(input(
            "Erro! Não pode ser negativo ou zero! \n" \
            "Digite o total da mercadoria que tem no estoque novamente: "
        ))
    valorCadaMercadoria = float(input("Digite o valor unitário de uma mercadoria: "))
    valorTotal = totalMercadorias * valorCadaMercadoria
    media = valorTotal / totalMercadorias
    print(
        f'Valor total do estoque R$ {valorTotal:.2f} \n'
        f'A média do valor das mercadorias é {media:.2f}'
        )
except ValueError:
    print("Erro, Por favor, digite corretamente.")