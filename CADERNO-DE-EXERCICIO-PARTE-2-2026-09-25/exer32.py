notas = []

for i in range(5):
    nota = float(input(f"Digite a nota do {i + 1}º aluno: "))
    notas.append(nota)

soma = 0

for nota in notas:
    soma += nota

media = soma / 5

acima = 0

for nota in notas:
    if nota > media:
        acima += 1

print(f"\nMédia da turma: {media:.2f}")
print(f"Alunos acima da média: {acima}")