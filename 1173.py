n1 = int(input())
vetor = [0]*10
vetor[0] = n1
for c in range(1,10):
    vetor[c] = 2*vetor[c-1]
for c in range(10):
    print(f'N[{c}] = {vetor[c]}')
