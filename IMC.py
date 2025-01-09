# Faça um algoritmo que calcule o IMC de uma pessoa, leia o seu peso 
# e sua altura e imprima na tela sua condição.

## Tabela Indíce de Massa Corporal (IMC)
print("Tabela IMC:")
print("Abaixo de 18,5 -> Abaixo do peso")          
print("Entre 18,6 e 24,9 -> Peso ideal (parabéns)")  
print("Entre 25,0 e 29,9 -> Levemente acima do peso")
print("Entre 30,0 e 34,9 -> Obesidade grau")
print("Entre 35,0 e 39,9 -> Obesidade grau II (severa)")
print("Maior ou igual a 40 -> Obesidade grau III (mórbida) \n ")

## Declaração de Variavéis
peso = float(input("Digite seu peso (Kg): "))
altura = float(input("Digite sua altura (M): "))
imc = peso / (altura * altura)

## Fazendo a verificação do imc
if imc == 18.5:
    print(f"Seu IMC: {imc} -> Abaixo do peso")
elif imc >= 18.6 and imc <= 24.9:
    print(f"Seu IMC: {imc} -> Peso ideal (parabéns)")
elif imc >= 25 and imc <= 29.9:
    print(f"Seu IMC: {imc} -> Levemente acima do peso")
elif imc >= 30 and imc <= 34.9:
    print(f"Seu IMC: {imc} -> Obesidade grau I")
elif imc >= 35 and imc <= 39.9:
    print(f"Seu IMC: {imc} -> Obesidade grau II (severa)")
else:
    print(f"Seu IMC: {imc} -> Obesidade grau III (mórbida)")