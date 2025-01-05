## Declaração de Variavéis
aluno = input("Por favor digite o nome do aluno: ")
nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))
soma = int(nota1 + nota2 + nota3)
media = int((nota1 + nota2 + nota3)/3)
resultado_final = media 

## Soma das notas
print ("O estudante ", aluno, " obteve suas notas somadas obtendo como resultado final: ", soma) 

## Média das notas
print ("Sua média aritimética foi de:", media)

## Verificação de aprovação
if resultado_final >= 8:
    print("Parabéns ", aluno, " você foi APROVADO")
else:
    print("Infelizmente ", aluno, " você foi REPROVADO")