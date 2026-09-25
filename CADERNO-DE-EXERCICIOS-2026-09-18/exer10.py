velocidade = float(input("Digite a velocidade do carro (km/h): "))

if velocidade > 80:
    excesso = velocidade - 80
    multa = excesso * 5
    print(f"Você foi multado! Valor da multa: R$ {multa:.2f}")
else:
    print("Boa viagem!")