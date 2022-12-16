# Escreva um algoritmo para ler as dimensões de um círculo (raio), calcular e escrever a área do círculo. a=pi*r²
import math

print("Área do cículo")

raio = int(input("Qual o valor do raio do círculo?"))

area = math.pi*(raio*raio)

print(round(area,2))