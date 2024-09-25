"""
Elabore um script que solicite o nome de 5 alunos e duas notas. 
Em seguida calcule e imprima a média e mostre se o aluno foi aprovado ou reprovado. 
Para esta aprovado a media tem de ser acima de 6,5.
"""

for i in range(5):
    
    nomeAluno = input(f"\nDigite o nome do aluno {i + 1}: ")
    
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    
    media = (nota1 + nota2) / 2
    
print(f"A média de {nomeAluno} é: {media:.2f}")
    
if media >= 6.5:
        print(f"{nomeAluno} foi aprovado!")
else:
        print(f"{nomeAluno} foi reprovado.")