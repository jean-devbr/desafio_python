# O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que o percentual do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo para ler o custo de fábrica de um carro, calcular e escrever o custo final ao consumidor.

percentual_distribuidor = 0.28
percentual_imposto = 0.45

custo_fabrica = float(input('Digite o valor de fabrica do carro: '))

distribuidor = custo_fabrica * percentual_distribuidor
imposto = custo_fabrica * percentual_imposto

consumidor = custo_fabrica + distribuidor + imposto

print(f'Você ia pagar pelo seu carro {consumidor}')