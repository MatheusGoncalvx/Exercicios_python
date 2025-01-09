# Faça um algoritmo que leia um valor qualquer e imprima na tela 
# com um reajuste de 5%.

## Declaração de Variáveis
num = float(input("Digite um valor: "))
reajuste = 5 / 100
result = num + (num * reajuste)  # Calculando o reajuste

## Exibindo resultado
print(f"O valor original é: {num}")
print(f"O valor com reajuste é: {result}")
