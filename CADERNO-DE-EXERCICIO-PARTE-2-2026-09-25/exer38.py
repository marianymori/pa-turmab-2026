import random

caminho = [0] * 10

minas = random.sample(range(10), 3)

for posicao in minas:
    caminho[posicao] = 1

print("Você tem 5 tentativas para atravessar o caminho.")

perdeu = False

for tentativa in range(5):
    posicao = int(input("\nEscolha uma posição de 0 a 9: "))

    if posicao < 0 or posicao > 9:
        print("Posição inválida!")
        continue

    if caminho[posicao] == 1:
        print("Você pisou em uma mina! Perdeu!")
        perdeu = True
        break
    else:
        print("Caminho livre!")

if not perdeu:
    print("\nParabéns! Você sobreviveu aos 5 passos e ganhou!")
