num = int(input("Digite o número para o calcular o fatorial: "))
fatorial = 1

for i in range(1, num + 1):
    fatorial *= i
    print(fatorial)