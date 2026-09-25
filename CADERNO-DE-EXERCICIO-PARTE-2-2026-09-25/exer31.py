numeros = []

for i in range(5):
    numero = int(input(f"Digite o {i + 1}º valor: "))
    numeros.append(numero)

print("\nOrdem normal:")

for numero in numeros:
    print(numero, end=" ")

print("\n\nOrdem inversa:")

for i in range(4, -1, -1):
    print(numeros[i], end=" ")