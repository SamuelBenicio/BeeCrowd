NOTAS = int(input())
print (NOTAS)

Q100 = NOTAS//100
NOTAS = NOTAS%100

Q50 = NOTAS//50
NOTAS = NOTAS%50

Q20 = NOTAS//20
NOTAS = NOTAS%20

Q10 = NOTAS//10
NOTAS = NOTAS%10

Q5 = NOTAS//5
NOTAS = NOTAS%5

Q2 = NOTAS//2
Q1 = NOTAS%2

print (f'{Q100} nota(s) de R$ 100,00')
print (f'{Q50} nota(s) de R$ 50,00')
print (f'{Q20} nota(s) de R$ 20,00')
print (f'{Q10} nota(s) de R$ 10,00')
print (f'{Q5} nota(s) de R$ 5,00')
print (f'{Q2} nota(s) de R$ 2,00')
print (f'{Q1} nota(s) de R$ 1,00')
