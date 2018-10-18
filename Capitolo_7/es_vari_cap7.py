''' esercizi vari cap  7'''

'''
a = 5
b = a
a = 3
print(b)
########
x=0
x = x+1
print(x)

########
def contoallarovescia(n):
    while n>0:
        print(n)
        n = n-1
    print('Via!')


contoallarovescia(int(input('Inserisci un numero: ')))

########


while True:
    riga =  input('> ')
    if riga == 'fine':
        break
    print(riga)

print('Finito!')


import math

epsilon=0.000000000000001

a = int(input('Inserisci a: '))
x = int(input('Inserisci x: '))

while True:
    print('X è',x)
    y = (x + a/x) /2
    if abs(y-x) < epsilon:
        break
    x = y

'''
def sequenza(n):
    while n!=1:
        print(n)
        if n%2 == 0: # n è pari
            n = n / 2
        else:
            n = n*3+1  #n è dispari

sequenza(int(input('Inserisci un numero: ')))

    
