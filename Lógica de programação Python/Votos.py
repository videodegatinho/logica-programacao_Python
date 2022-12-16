#Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos brancos, nulos e válidos.
# Calcular e escrever o percentual que cada um representa em relação ao total de eleitores.

print("Calculo do percentual")

brancos = int(input("Digite o número de votos brancos: "))
nulos = int(input("Digite o número de votos nulos: "))
validos = int(input("Digite o número de votos válidos: "))

totalEleitores = (brancos+nulos+validos)

percentualBrancos = (brancos/totalEleitores) * 100
percentualNulos = (nulos/totalEleitores) * 100
percentualValidos = (validos/totalEleitores) * 100

print(percentualBrancos)
print(percentualNulos)
print(percentualValidos)