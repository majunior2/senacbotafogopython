"Elabore um script que solicite o nome de um aluno e duas notas."
"Em seguida calcule e imprima a media e mostre se o aluno foi aprovado ou reprovado, Para estar aprovado a media tem de ser acima de 6,5"
"Faca isso para 3 alunos" " pedir todos alunos e notas e no final fazer a listagem" 

resultados = []
for i in range(3):
    nomeAluno =input(f'Digite o nome do aluno{i +1}: ')
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1+nota2)/2

    situação  = "Aprovado" if media >= 6.5 else "Reprovado"

    resultados.append((nomeAluno, media, situação))

print("\nListagem de Resultados:")
print(f"{'Nome do Aluno':<20} {'Média':<10} {'Situação'}")
for nome, media, situacao in resultados:
    print(f"{nome:<20} {media:.2f}<10 {situacao}")




# o for é um looping especializado em ler lista