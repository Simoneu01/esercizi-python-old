'''
Esercizio 7.1. Copiate il ciclo del Paragrafo 7.5 e incapsulatelo in una funzione di nome mia_radq
che prenda a come parametro, scelga un valore appropriato di x, e restituisca una stima del valore
della radice quadrata di a.
'''

import math

epsilon=0.00000000000000001

def mia_radq(a):
    x = 3
    while True:
        y = (x + a/x) /2
        if abs(y-x) < epsilon:
            break
        x = y
    return x


def test_radq():
    print('a',' '*(25-len('mia_radq(a)')),'mia_radq(a)',' '*(25-len('math.sqrt(a)')),'math.sqrt(a)',' '*(25-len('diff')),'diff')
    print('-',' '*(25-len('mia_radq(a)')),'-----------',' '*(25-len('math.sqrt(a)')),'------------',' '*(25-len('diff')),'----')
    i=1
    while i<10:
        mia_radq(i)
        diff=abs(mia_radq(i)-math.sqrt(i))
        print(str(i),' '*(25-len(str(mia_radq(i)))),str(mia_radq(i)),' '*(25-len(str(math.sqrt(i)))),str(math.sqrt(i)),' '*(25-len(str(diff))),str(diff))
        i=i+1
        
test_radq()
