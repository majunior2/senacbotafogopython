tenho_sede = True
tenho_fome = True

if tenho_fome and tenho_sede:
    print("Comprar sanduiche e Coca-cola!")
elif tenho_sede and not tenho_fome:
    print("Comprar Coca-cola")
elif not(tenho_sede) and tenho_fome :
    print("Compra Snaduiche")
else:
    print("Não gastar dinheiro")
