# solicito o usuário para digitar um número 
numero = int(input("Digite um numero para tabuada de 10"))
# inicializa o número 
i = 1
while i <= 10:
    aux = i * numero
    print(i ,"x",numero ,"= ",aux)
    i = i + 1
