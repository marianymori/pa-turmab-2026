numeros = []

for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

print("\nPosições e valores:")

for i in range(5):
    print(f"Índice: {i} | Valor: {numeros[i]}")