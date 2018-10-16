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




