n = 1
soma = 0
i=0
while(n>0):
  i +=1
  n = int(input())
  if(n>0):
    soma +=n
    media = soma/i
print(f'{media:.2f}')
