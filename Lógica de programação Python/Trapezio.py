# Escreva um algoritmo para ler as dimensões de um trapézio (base maior, base menor e altura), calcular e escrever a área do trapézio.
# a=(B+b).h/2

print("Área do trapézio")

baseMaior = int(input("Digite o valor da base maior: "))
baseMenor = int(input("Digite o valor da base menor: "))
altura = int(input("Digite o valor da altura: "))

area = (baseMaior+baseMenor)*altura/2
print(area)