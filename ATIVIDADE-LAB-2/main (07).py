total_pontos = 0

for i in range(1, 6):
    nota = float(input(f"Digite a {i}ª nota: "))
    total_pontos += nota

media = total_pontos / 5

print("Total de pontos:", total_pontos)
print("Média:", media)

if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")