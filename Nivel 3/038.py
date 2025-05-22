# Faça um algoritmo para ler um número que é um código de usuário. Caso este código seja diferente de um código armazenado internamente no algoritmo (igual a 1234) deve ser apresentada a mensagem ‘Usuário inválido!’. Caso o Código seja correto, deve ser lido outro valor que é a senha. Se esta senha estiver incorreta (a certa é 9999) deve ser mostrada a mensagem ‘senha incorreta’. Caso a senha esteja correta, deve ser mostrada a mensagem ‘Acesso permitido’.

codigo = int(input("Digite o código de usuário: "))
while codigo != 1234:
        print("Usuário inválido!")
        codigo = int(input("Digite o código de usuário novamente: "))
    
senha = int(input("Digite a senha: "))
while senha != 9999:
        print("Senha incorreta!")
        senha = int(input("Digite a senha novamente: ")) 

print("Acesso permitido")