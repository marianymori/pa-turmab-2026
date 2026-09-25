valor = float(input("Digite o valor original do produto: R$ "))

desconto = valor * 0.15
valor_final = valor - desconto

print(f"Valor do desconto: R$ {desconto:.2f}")
print(f"Valor com desconto: R$ {valor_final:.2f}")