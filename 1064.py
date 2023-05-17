cont = 0
i = 0
pos = 0
soma = 0
while(i!=6):
  n = float(input())
  i +=1
  if(n>0):
    pos+=1
    soma +=n
    media = soma/pos
print(f'{pos} valores positivos')
print(f'{media:.1f}')
