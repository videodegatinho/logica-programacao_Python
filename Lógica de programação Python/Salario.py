#Escreva um algoritmo para ler o salário mensal atual de um funcionário e o percentual de reajuste.
# Calcular e escrever o valor do novo salário.

print("Valor do novo salário.")

salario = float(input("Digite o seu salário atual: "))
percentualReajuste = float(input("Digite o valor do percentual de reajuste: "))

novoSalario = (salario*(percentualReajuste/100))+salario

print(novoSalario)
