a = float(input("Digite o primeiro lado: "))
b = float(input("Digite o segundo lado: "))
c = float(input("Digite o terceiro lado: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Triângulo EQUILÁTERO")
    elif a == b or a == c or b == c:
        print("Triângulo ISÓSCELES")
    else:
        print("Triângulo ESCALENO")
else:
    print("Os segmentos não podem formar um triângulo.")