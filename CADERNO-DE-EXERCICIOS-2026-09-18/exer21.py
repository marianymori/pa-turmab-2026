quantidade = 0
soma = 0

while True:
    numero = int(input("Digite um número inteiro (0 para parar): "))

    if numero == 0:
        break

    quantidade += 1
    soma += numero

print(f"Quantidade de números digitados: {quantidade}")
print(f"Soma dos números: {soma}")