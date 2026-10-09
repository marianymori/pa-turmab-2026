def inicio():
    vetor = []
    
    n = int(input("Quantos números deseja digitar? "))
    
    # Leitura dos dados
    for i in range(n):
        valor = int(input(f"Digite o valor {i}: "))
        vetor.append(valor)
        
    # Bubble sort: n-1 passagens, comparando vizinhos
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if vetor[j] > vetor[j + 1]:
                # Troca de valores
                temp = vetor[j]
                vetor[j] = vetor[j + 1]
                vetor[j + 1] = temp
                
    # Exibição do vetor ordenado
    print("Vetor ordenado: ", end="")
    for i in range(n):
        print(f"{vetor[i]} ", end="")
    print()

# Executa a função
inicio()
