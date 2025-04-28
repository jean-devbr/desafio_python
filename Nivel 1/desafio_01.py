#faça um algorítimo que mostre a tabuada de 1 a 5

print("Digite ok para mostrar tabuada!")
ok = input().strip().lower() # Remover o expaço em branco (extras) e converte para minúsculo
if ok == "ok":
    for numero in range(1, 6): # Primeiro for para os números de 1 a 5
        print(f"\nTabuada do {numero}:") # Exibe qual tabuada está sendo mostrada
        for i in range(1, 11): # Segundo for para multiplicar de 1 a 10 
             print(f"{numero} x {i} = {numero * i}")        
else: 
    print("Você não digitou 'ok', então não será exibida a tabuada.")
