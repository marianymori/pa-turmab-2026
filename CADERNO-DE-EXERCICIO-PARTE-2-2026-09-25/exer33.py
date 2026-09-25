valor = int(input("Digite o valor do saque: "))

notas50 = valor // 50
valor = valor % 50

notas20 = valor // 20
valor = valor % 20

notas10 = valor // 10
valor = valor % 10

notas1 = valor

print("\nNotas entregues:")
print(f"R$50: {notas50}")
print(f"R$20: {notas20}")
print(f"R$10: {notas10}")
print(f"R$1: {notas1}")