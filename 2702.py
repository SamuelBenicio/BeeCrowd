frango = 0
bife = 0
massa = 0
n1,n2,n3 = map(int,input().split(' '))
n4,n5,n6 = map(int,input().split(' '))
if(n4>n1):
    frango = n4-n1
if(n5>n2):
    bife = n5-n2
if(n6>n3):
    massa = n6-n3
total = massa+frango+bife
print(f'{total}')
