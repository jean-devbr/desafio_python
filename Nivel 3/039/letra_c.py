# Para A = V, B = V e C = F, qual o resultado da avaliação das seguintes expressões:
#letra C: A ou C e B xou A e não B 
A = True
B = True
C = False
resultado = A or C and (B != A) and A and not B
print(resultado)  # Saída: False
