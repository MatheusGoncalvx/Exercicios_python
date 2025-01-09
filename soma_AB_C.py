# Faça um algoritmo que leia os valores de A, B, C e em seguida 
# imprima na tela a soma entre A e B é mostre se a soma é menor que C.

## Declaração de Variavéis
A = int(input("Digite o 1º número para somar: "))
B = int(input("Digite o 2º número para somar: "))
C = int(19)
soma = A + B

## Imprimindo os resultados
print(f"Números: {A} {B} {C}")
print(f"Soma das variavéis A e B: {soma}")

## Fazendo a verificação se a soma entre os números é menor que C
if soma < C:
    print(f"A soma entre os números digitados resultou em {soma}, número maior que {C}")
else:
    print("A soma entre os números digitados é maior ou igual o último número!!!")