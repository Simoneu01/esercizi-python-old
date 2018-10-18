'''
Esercizio 7.2. La funzione predefinita eval valuta un’espressione sotto forma di stringa, usando
l’interprete Python.
'''
import math

def eval_ciclo():
    while True:
        riga =  input('> ')
        if riga == 'fatto':
            break
        x=eval(riga)
        print(x)
    print('Finito!')
    return x

print(eval_ciclo())

nomi1 = 5
nomi2 = 6
nomi3 = 7

for i in range (1,4):
    print('nomi{}'.format(i))
