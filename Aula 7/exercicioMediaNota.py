"""
Elabore um script que solicite o nome de um aluno e duas notas. 
Em seguida calcule e imprima a média e mostre se o aluno foi aprovado ou reprovado. 
Para esta aprovado a media tem de ser acima de 6,5.
"""

nomeAluno = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunta nota: "))

media = (nota1 + nota2) / 2

print(f"a média de {nomeAluno} é: {media: .2f}")

if media >= 6.5:
    print(f"{nomeAluno} esta Aprovado")
else:
    print(f"{nomeAluno} esta reprovado")


