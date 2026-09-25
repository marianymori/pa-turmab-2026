nomes = []
idades = []

while True:
    print("\n===== MENU =====")
    print("1 - Cadastrar")
    print("2 - Listar maiores de 18 anos")
    print("3 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))

        nomes.append(nome)
        idades.append(idade)

        print("Pessoa cadastrada!")

    elif opcao == 2:
        print("\nPessoas maiores de 18 anos:")

        for i in range(len(nomes)):
            if idades[i] > 18:
                print(f"{nomes[i]} - {idades[i]} anos")

    elif opcao == 3:
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")