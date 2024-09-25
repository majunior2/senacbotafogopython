"""
altera o script odo ultimo eercicio para que a idade for maior que 50 anos,
 a mensagem seja: fulano tem x anos e é experiente.
se a idade for menor que 50 anos, a mensagem deve ser: fulano tem x anos, está em treinamento
"""

#idade = int(input("Digite a sua idade: "))

#if idade > 50:
    #print(f"Fulano tem {idade} anos e é experiente.")
#else:
    #print(f"Fulano tem {idade} anos, está em treinamento.")

#correção

nome = input('Digite o nome: ')
idade = int(input('Digite a idade: '))

if idade > 50:
    print(f"{nome} tem {idade} anos e é experiente ")
else:
    print(f"{nome} tem {idade} e está em treinamento ")


#print(nome,"tem",idade,"anos e é experiente")
