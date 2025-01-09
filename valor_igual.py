# Faça um algoritmo que leia dois valores inteiros A e B, se os valores 
# de A e B forem iguais, deverá somar os dois valores caso contrário devera 
# multiplicar A por B. Ao final de qualquer um dos cálculos deve-se atribuir 
# o resultado a uma variável C e imprimir seu valor na tela.

##  Declaração de Variavéis
A = int(input("Digite o 1º número: "))
B = int(input("Digite o 2º número: " ))

## Fazendo a verificação lógica
if A == B:
    C = A + B
    print(f"Os números digitados são iguais, portanto sua soma é: {C}.")
else:
    C = A * B
    print(f"Os números digitados são iguais, portanto sua multiplicação é: {C}.")
