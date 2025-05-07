# Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu).

ano = 2025
ano_nascimento = int(input('Digite o ano que você nasceu: '))
resultado = ano - ano_nascimento

if resultado >= 18:
    print(f'Você poderá votar esse ano.\nVocê nasceu no ano {ano_nascimento} e tem {resultado} anos.')

else:
    print(f'Você NÃO poderá votar esse ano.\nVocê nasceu no ano {ano_nascimento} e tem {resultado} anos')    

    
