# Uma empresa quer verificar se um empregado está qualificado para a aposentadoria ou não. Para estar em condições, um dos seguintes requisitos deve ser satisfeito:
# - Ter no mínimo 65 anos de idade.
# - Ter trabalhado no mínimo 30 anos.
# - Ter no mínimo 60 anos e ter trabalhado no mínimo 25 anos.
# Com base nas informações acima, faça um algoritmo que leia: o número do empregado (código), o ano de seu nascimento e o ano de seu ingresso na empresa. O programa deverá escrever a idade e o tempo de trabalho do empregado e a mensagem 'Requerer aposentadoria' ou 'Não requerer'.

from datetime import datetime
try:
    numeroEmprego = int(input("Digite seu código de trabalho: "))
    while numeroEmprego < 0:
        numeroEmprego = int(input("Erro! Por favor digite o código positivo! \nDigite seu código de trabalho: "))
    anoNascimento = int(input("Digite o ano que você nasceu: "))
    while anoNascimento < 0:
        anoNascimento = int(input("Erro! Por favor, digite o ano nascimento correto apénas positivo. \nDigite o ano que você nasceu: "))
    ingressoEmpresa = int(input("Digite o ano que você começou trabalha na empresa: "))
    while ingressoEmpresa < 0 or ingressoEmpresa > datetime.now().year:
        ingressoEmpresa = int(input("Erro! Por favor, digite o ano que você entrou na empresa correto(positivo). \nDigite o ano que você começou na trabalha na empresa: "))
    anoAtual = datetime.now().year # Obtém o ano atual dinamicamente
    idade = anoAtual - anoNascimento
    periodoEmpresa = anoAtual - ingressoEmpresa

    if idade >= 65:
        print(f"O dono do código {numeroEmprego}\nSua idade é {idade} \nSeu período na empresa é {periodoEmpresa} \nRequerer aposentadoria!")
    elif periodoEmpresa >= 30:
        print(f"O dono do código {numeroEmprego} \nSeu idade é {idade} \nSeu período na empresa é {periodoEmpresa} \nRequerer aposentadoria!")
    elif idade >= 60 and periodoEmpresa >= 25:
        print(f'O dono do código {numeroEmprego} \nSeu idade é {idade} \nSeu período na empresa é {periodoEmpresa} \nRequerer aposentadoria!')
    else:
        print(f'O dono do código {numeroEmprego} \nSeu idade é {idade} \nSeu período na empresa é {periodoEmpresa} \nNão requerer aposentadoria!')
except ValueError:
    print("Erro! Por favor, Digite corretamente as informações!")