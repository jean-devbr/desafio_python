#Escreva um algoritmo para ler um valor numérico (do teclado) e escrever (na tela) o seu antecessor

numero = float(input("Digite um valor qualquer: ")) #float: server para colocar numeros não inteiros
antecessor = numero - 1 #serve para subtrair do numero 
print("O antecessor do", numero , "é:" ,antecessor)  #entre as virgulas serve para fazer uma interpolação de strings, invés do f 
