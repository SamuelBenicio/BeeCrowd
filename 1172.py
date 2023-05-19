vetor = []
for c in range(10):
    x = int(input())
    vetor.append(x)
for i in range(10):
    if(vetor[i]<=0):
        vetor[i] = 1
for v in range(10):
    print(f'X[{v}] = {vetor[v]}')

