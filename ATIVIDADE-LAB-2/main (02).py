a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

soma = a + b
subtracao = a - b
multiplicacao = a * b

print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)

if b != 0:
    divisao = a / b
    print("Divisão:", divisao)
else:
    print("Não é possível dividir por zero.")