# Faça um algoritmo que leia o valor de um produto e determine o valor que deve ser pago, conforme 
# a escolha da forma de pagamento pelo comprador e imprima na tela o valor final do produto a ser pago. 
# Utilize os códigos da tabela de condições de pagamento para efetuar o cálculo adequado.

## Declaração de Variavéis
produto = float(1500.00)
forma_pagamento = input("Escolha a forma de pagamento (Dinheiro, Pix, Crédito): ")

print(f"Valor do produto: {produto}")

if forma_pagamento == "Dinheiro" or forma_pagamento == "Pix":
    desconto = 15 / 100
    preco_final = produto - (produto * desconto)
    print(f"O valor a ser pago é de: {preco_final}")
elif forma_pagamento == "Credito" or forma_pagamento == "credito" or forma_pagamento == "Crédito" or forma_pagamento == "crédito":
    print("Escolha uma opção: ")
    forma_pagamento = input(" 1 Vez \n 2 Vezes sem juros\n 3 Vezes + 10% de juros \n")
    if forma_pagamento == "1 vez" or forma_pagamento == "1 Vez" or forma_pagamento == "1":
        desconto = 10 / 100
        preco_final = produto - (produto * desconto)
        print(f"O valor a ser pago é de: {preco_final} reais") 
    elif forma_pagamento == "2 vezes" or forma_pagamento == "2 Vezes" or forma_pagamento == "2":
        preco_final = produto / 2
        print(f"O valor a ser pago parcelado em duas vezes é de: {preco_final} reais sem juros")
    elif forma_pagamento == "3 vezes" or forma_pagamento == "3 Vezes" or forma_pagamento == "3":
        juros = 10 / 100
        preco_final = (produto / 3) + produto * juros
        print(f"O valor a ser pago parcelado em três vezes é de: {preco_final} reais com 10% de juros")