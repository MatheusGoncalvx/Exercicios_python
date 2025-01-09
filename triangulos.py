# Faça um algoritmo que leia três valores que representam os três lados de 
# um triângulo e verifique se são válidos, determine se o triângulo é 
# equilátero, isósceles ou escaleno.

## Declaração de Variáveis
ladoA = int(input("Digite o primeiro lado: "))
ladoB = int(input("Digite o segundo lado: "))
ladoC = int(input("Digite o terceiro lado: "))

## Verificando se os lados formam um triângulo válido
if ladoA + ladoB > ladoC and ladoA + ladoC > ladoB and ladoB + ladoC > ladoA:
    # Verificando o tipo do triângulo
    if ladoA == ladoB == ladoC:
        print("Triângulo equilátero")
    elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
        print("Triângulo isósceles")
    else:
        print("Triângulo escaleno")
else:
    print("Os valores fornecidos não formam um triângulo.")
