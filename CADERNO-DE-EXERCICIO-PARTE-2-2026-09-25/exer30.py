nomes = []
notas = []

for i in range(3):
    nome = input(f"Digite o nome do {i + 1}º aluno: ")
    nota = float(input("Digite a nota: "))

    nomes.append(nome)
    notas.append(nota)

print("\nResultados:")

for i in range(3):
    print(f"\nNome: {nomes[i]}")
    print(f"Nota: {notas[i]}")

    if notas[i] >= 7:
        print("Situação: Aprovado")
    else:
        print("Situação: Reprovado")