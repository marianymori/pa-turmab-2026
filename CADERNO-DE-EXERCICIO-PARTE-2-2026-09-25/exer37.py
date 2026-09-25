produtos = []
estoques = []

while True:
    print("\n===== ESTOQUE =====")
    print("1 - Adicionar Produto")
    print("2 - Dar Baixa")
    print("3 - Ver Estoque")
    print("4 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        nome = input("Nome do produto: ")
        quantidade = int(input("Quantidade: "))

        produtos.append(nome)
        estoques.append(quantidade)

        print("Produto adicionado!")

    elif opcao == 2:
        nome = input("Nome do produto: ")

        if nome in produtos:
            posicao = produtos.index(nome)

            quantidade = int(input("Quantidade para retirar: "))

            if quantidade <= estoques[posicao]:
                estoques[posicao] -= quantidade
                print("Baixa realizada!")
            else:
                print("Estoque insuficiente!")
        else:
            print("Produto não encontrado!")

    elif opcao == 3:
        print("\n===== ESTOQUE ATUAL =====")

        for i in range(len(produtos)):
            print(f"{produtos[i]} - {estoques[i]} unidades")

    elif opcao == 4:
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")