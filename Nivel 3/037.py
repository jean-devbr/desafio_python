# Uma fruteira está vendendo frutas com a seguinte tabela de preços: 
#Até        5 Kg Acima de 5 Kg
#Morango R$ 2,50 por Kg R$ 2,20 por Kg
#Maçã R$ 1,80 por Kg R$ 1,50 por Kg 
#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente. 
morango = int(input("Quantos kg você quer de morango: "))
if morango <= 5:
    preco_final_morango = morango * 2.5
else:
    preco_final_morango = morango * 2.2
maca = int(input("Quantos kg você quer de maçã: "))
if maca <= 5:
    preco_final_maca = maca * 1.8
else:
    preco_final_maca = maca * 1.5

quantidade_frutas = morango + maca
preco_final_total_bruto = preco_final_maca + preco_final_morango

if quantidade_frutas >= 8 or preco_final_total_bruto > 25:
    preco_final_total = preco_final_total_bruto * 0.90
else:
    preco_final_total = preco_final_maca + preco_final_morango

print(f'Você pediu {morango} em kg e vai paga pelo valor de cada uma {preco_final_morango:.2f} \nVocê pediu {maca} em kg e vai paga pelo valor de cada uma {preco_final_maca:.2f} \nTotal de fruta que você comprou foi de {quantidade_frutas} e vai pagar pelo valor total da comprar {preco_final_total:.2f}') 


    



           
