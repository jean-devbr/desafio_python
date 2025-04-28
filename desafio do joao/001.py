"""
Criar um jogo onde o computador escolhe um número aleatório entre 1 e 100, e o
usuário tem que adivinhar qual é esse número. A cada tentativa do usuário, o programa
deve fornecer dicas para ajudá-lo a adivinhar corretamente, como "muito alto", "muito
baixo", ou "correto".
"""
import random # Biblioteca para gerar números aleatorios 
numero = random.randint(1, 100) # Um número aleatório, randint (retorna o número inteiro aleatorio)
tentativas = 10
print("Tenter advinhar o número que estou pensando entre 1 até 100!")

while tentativas > 0: 
    escolhe = int(input("Escolha um número entre 1 a 100! "))
    if escolhe == numero:
        print("Você acertou!")
        break # Sair do loop
    elif escolhe > numero: 
        print("Você ERROU! O número é muito alto") 
    elif escolhe < numero:
        print("Você ERROU! O número é muito baixo") 
    
    tentativas -= 1 # Vai diminuindo as tentativas 
    print(f'Você ainda tem {tentativas} tentativas restantes.')

if tentativas == 0:
    print("Você usou todas suas tentativas!")