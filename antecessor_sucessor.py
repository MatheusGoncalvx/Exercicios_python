# Faça um algoritmo que receba um número inteiro e imprima na tela o 
# seu antecessor e o seu sucessor.

## Declaração de Variavéis
num = int(input("Digite um número: "))

## Lógica de antecessor e sucessor:
antecessor = num - 1
sucessor = num + 1

## Exibindo resultados
print(f"O número digitado foi {num} seu antecessor é {antecessor} e sucessor é {sucessor}, logo o resultado final é: {antecessor} {num} {sucessor}")
