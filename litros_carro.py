# Faça um algoritmo que calcule a quantidade de litros de combustível gastos em
# uma viagem, sabendo que o carro faz 12km com um litro. Deve-se fornecer ao
# usuário o tempo que será gasto na viagem a sua velocidade média, distância
# percorrida e a quantidade de litros utilizados para fazer a viagem.

## Declaração de Variáveis
tempo = float(input("Digite o tempo gasto na viagem (em horas): "))
velocidade = float(input("Digite a velocidade média durante a viagem (em km/h): "))

# Cálculo da distância percorrida
distancia = tempo * velocidade

# Cálculo da quantidade de litros de combustível utilizados
litros_usados = distancia / 12

# Exibindo os resultados
print(f"\nDistância percorrida: {distancia} km")
print(f"Quantidade de combustível utilizada: {litros_usados} litros")
