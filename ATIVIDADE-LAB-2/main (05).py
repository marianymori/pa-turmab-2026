a = float(input("Digite o lado A: "))
b = float(input("Digite o lado B: "))
c = float(input("Digite o lado C: "))

if a + b > c and a + c > b and b + c > a:
    print("Triângulo válido")

    if a == b and b == c:
        print("Triângulo equilátero")
    elif a == b or a == c or b == c:
        print("Triângulo isósceles")
    else:
        print("Triângulo escaleno")
else:
    print("Os lados não formam um triângulo válido")