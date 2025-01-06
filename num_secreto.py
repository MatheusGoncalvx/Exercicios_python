## Declaração de Variavéis
user = int(input("Digite um número: "))
num = 7

## Verificando se o número for diferente do que o user digitar
while user != num:
    if user < num:
        print(" Tente um número maior ")
    else:
        print(" Tente um número menor ")
    
    user = int(input("Digite outro numéro: "))

    if user == num:
        print("Parabéns você acertou o número secreto!!!")