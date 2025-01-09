## Exibindo menu de opções
def exibir_menu():
    print("\n Escolha uma operação: ")
    print(" Soma -> 1")
    print(" Subtração -> 2")
    print(" Multiplicação -> 3")
    print(" Divisão -> 4")
    print(" Sair -> 0")

## Declarando funções das operações
def soma(num1, num2):
    result = num1 + num2
    print(result)

def subtracao(num1, num2):
    result = num1 - num2
    print(result)

def multiplicacao(num1, num2):
    result = num1 * num2
    print(result)

def divisao(num1, num2):
    if num2 == 0:  # Evita divisão por zero
        print("Erro: Divisão por zero não é permitida.")
    else:
        result = num1 / num2
        print(result)

## Função principal
while True:  # Laço para repetir o menu até o usuário decidir sair
    exibir_menu()
    opcao = int(input("Digite sua escolha: "))

    if opcao == 0:  # Sai do programa
        print("Encerrando o programa. Até logo!")
        break
    elif opcao in [1, 2, 3, 4]:  # Opções válidas
        num1 = int(input("Digite o 1º número: "))
        num2 = int(input("Digite o 2º número: "))

        if opcao == 1:
            soma(num1, num2)
        elif opcao == 2:
            subtracao(num1, num2)
        elif opcao == 3:
            multiplicacao(num1, num2)
        elif opcao == 4:
            divisao(num1, num2)
    else:  # Tratamento para opções inválidas
        print("Opção inválida. Tente novamente.")
