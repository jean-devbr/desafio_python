#Pedi a senha até que seja digitada a correta

senha = input("Digite a senha até 4 letras: ")
while senha != "jean":
    print("Erro: Senha incorreta!")
    senha = input("Digite a senha novamente! ")
print("A senha esta corretar")