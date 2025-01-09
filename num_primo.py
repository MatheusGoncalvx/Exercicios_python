# Solicita um número ao usuário
num = int(input("Digite um número para verificar se ele é primo: "))

# Verifica se o número é menor ou igual a 1
if num <= 1:
    print("Este número não é primo.")
else:
    # Verifica se o número tem divisores além de 1 e ele mesmo
    num_primo = True
    for i in range(2, num):
        if num % i == 0:
            num_primo = False
            break

    # Exibe o resultado
    if num_primo:
        print(f"O número {num} é primo.")
    else:
        print(f"O número {num} não é primo.")
