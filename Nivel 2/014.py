# Sequência de Fibonacci
# Escreva um programa que gere os primeiros 10 números da sequência de Fibonacci.

a, b = 0, 1
print('Os primeiros 10 números da sequência de fibonnaci são: ')
for _ in range(10):
    print(a)
    a, b = b , a + b
