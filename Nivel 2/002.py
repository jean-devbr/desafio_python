#Peça ao usuário para digitar a idade e classifique a pessoa em uma das seguintes categorias:

#Menor de idade (0 a 17 anos)
#Adulto (18 a 64 anos)
#Idoso (65 anos ou mais)

num = int(input("Digite sua idade: "))

if num <=17:
    print("Você é menor de idade")
elif num <=64:
    print("Você é um adulto")
else:
    print("Você é um idoso")
