poltronas = [False] * 10

while True:
    print("\nMapa das poltronas:")

    for i in range(10):
        if poltronas[i]:
            print("[X]", end=" ")
        else:
            print("[ ]", end=" ")

    print()

    numero = int(input("Digite o número da poltrona (-1 para sair): "))

    if numero < 0:
        break

    if numero > 9:
        print("Poltrona inválida!")
        continue

    if poltronas[numero]:
        print("Ocupada!")
    else:
        poltronas[numero] = True
        print("Reservada!")

print("\nPrograma encerrado.")