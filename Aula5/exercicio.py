lista = []

while True:
    numero = int(input("Digite um número (0 - sai) : "))
    if numero == 0:
        break
    lista.append(numero)


# o while não pode ser convertido em for porque
# o número de repetições é desconhecido no inicio
for i in lista:
    print(i)