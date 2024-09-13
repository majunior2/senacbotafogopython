"""Escreva um programa que calcule o aumento  de salário
ele deve solicitar o valor do salario
e a porcentagem de aumento do novo salário.
Exiba o valor do aumento e do novo salário"""
#Entrada-> solicito o usuário que digite uma informação
salario =  float(input("Digite o valor do salário"))
print("O Salário informado foi de ")
aumento = float(input("Digite o percentual de aumento"))
print("0 percentual informado foi de ",aumento)
# processamento (variable) salario: float
novosalario = salario +(salario * aumento)/100
#saída
print("O valor do aumento é R$", aumento)

print("O novo salário é :", novosalario)