nome = ""
conta = ""
saldo = 0
criada = False

while True:
    print("\n===== BANCO =====")
    print("1 - Criar Conta")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Extrato / Ver Saldo")
    print("5 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        nome = input("Digite seu nome: ")
        conta = input("Digite o número da conta: ")

        saldo = 0
        criada = True

        print("Conta criada com sucesso!")

    elif opcao == 2:
        if criada:
            valor = float(input("Digite o valor para depositar: "))

            if valor > 0:
                saldo += valor
                print("Depósito realizado!")
            else:
                print("Valor inválido!")
        else:
            print("Crie uma conta primeiro!")

    elif opcao == 3:
        if criada:
            valor = float(input("Digite o valor para sacar: "))

            if valor <= 0:
                print("Valor inválido!")
            elif valor <= saldo:
                saldo -= valor
                print("Saque realizado!")
            else:
                print("Saldo insuficiente!")
        else:
            print("Crie uma conta primeiro!")

    elif opcao == 4:
        if criada:
            print("\n===== EXTRATO =====")
            print(f"Nome: {nome}")
            print(f"Conta: {conta}")
            print(f"Saldo: R$ {saldo:.2f}")
        else:
            print("Crie uma conta primeiro!")

    elif opcao == 5:
        print("Obrigado por utilizar o banco!")
        break

    else:
        print("Opção inválida!")