#Tabuada
#Escreva um programa que peça um número ao usuário e imprima a tabuada desse número de 1 a 10.
num = int(input('Digite um número: '))
print(f'Tabuada do número {num}')
for i in range(1,11):
    resultado = num * i 
    print(f'{num} x {i} = {resultado:}')