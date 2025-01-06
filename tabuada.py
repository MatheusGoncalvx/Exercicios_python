## Declaração de Variavéis
num = int(input("Digite o número da tabuda que deseja saber: "))

## Realizando verificação
for i in range(11):
    result = i * num
    print(num, "*", i, "=", result)