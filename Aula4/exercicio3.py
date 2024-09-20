"""
Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$
0,45 para viagens mais longas.
"""
distancia = float(input("Digite a distancia que você deseja percorrer"))
print(f'A distancia que voce deseja percorrer é de {distancia} km.')
tarifa_curta = 0.50
tarifa_longa = 0.45

if distancia <= 200:
     preco = distancia * tarifa_curta
else:
     preco = distancia * tarifa_longa

print(f'O preço da passagem para {distancia:.2f} km é R${ preco:.2f}.')

#CORREÇÃO
#km = float(input("Digite a distancia percorrida"))

#if km <= 200:
#   passagem  = 0.5 * km

#else km > 200:
#   passagem  = 0.45 * km
#print(f'O valor a pagar por percorrer {km} é R${passagem})