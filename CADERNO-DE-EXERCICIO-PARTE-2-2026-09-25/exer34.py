votos = [0, 0, 0, 0, 0]

print("1 - João")
print("2 - Maria")
print("3 - José")
print("4 - Nulo")
print("5 - Branco")
print("0 - Encerrar")

while True:
    voto = int(input("\nDigite seu voto: "))

    if voto == 0:
        break

    if voto >= 1 and voto <= 5:
        votos[voto - 1] += 1
    else:
        print("Voto inválido!")

print("\n===== RESULTADO =====")
print(f"João: {votos[0]} voto(s)")
print(f"Maria: {votos[1]} voto(s)")
print(f"José: {votos[2]} voto(s)")
print(f"Nulos: {votos[3]} voto(s)")
print(f"Brancos: {votos[4]} voto(s)")

maior = max(votos[0:3])

if votos[0] == maior:
    print("Vencedor: João")
elif votos[1] == maior:
    print("Vencedor: Maria")
elif votos[2] == maior:
    print("Vencedor: José")