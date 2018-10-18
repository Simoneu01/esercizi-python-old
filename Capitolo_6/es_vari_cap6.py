import math

def area(x):
    if type(x) != int or type(x) != float: return area(eval(input('Iserisci un numero: ')))
    a = math.pi * x**2
    return a

def area1(x):
    return math.pi * x**2

def valore_assoluto(x):
    if x < 0:
        return -x
    else:
        return x
def distanza(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquadr = dx**2 + dy**2
    risultato = math.sqrt(dsquadr)
    return risultato

def area_cerchio(x1, y1, x2, y2):
    return area(distanza(x1, y1, x2, y2))

def divisibile(x, y):
    if x % y == 0: return True
    return False

def compreso_tra(x, y, z):
    if x>y:
        return False
    elif z<y:
        return False
    return True

def fattoriale(x):
    if x == 0:
        return 1
    else:
        ricors = fattoriale(x-1)
        risultato = x * ricors
    return risultato

funzioni='''

0 = Funzione area con return
1 = Funzione area senza return
2 = Funzione valore assoluto
3 = Funzione distanza
4 = Funzione area_cerchio
5 = Funzione divisibile
6 = Funzione compreso_tra
7 = Funzione fattoriale
'''

'''y='n'
while y!='n':
    print(funzioni)
    x=int(input('Che funzione vuoi provare? [0-9] '))
    if x==0:
        print('Hai selezionato la funzione area con return')
        print('Il raggio è:' , area(int(input('Inserisci il raggio: '))))
    elif x==1:
        print('\nHai selezionato la funzione area senza return')
        print('Il raggio è:' , area1(int(input('Inserisci il raggio: '))))
    elif x==2:
        print('\nHai selezionato la funzione valore assoluto')
        print(valore_assoluto(int(input('Inserisci un valore: '))))
    elif x==3:
        print('\nHai selezionato la funzione distanza')
        print(distanza(int(input('Inserisci x1: ')),int(input('Inserisci y1: ')),int(input('Inserisci x2: ')),int(input('Inserisci y2: '))))
    elif x==4:
        print('\nHai selezionato la funzione area cerchio')
        print("L'area del cerchio è:",area_cerchio(int(input('Inserisci xc: ')),int(input('Inserisci yc: ')),int(input('Inserisci xp: ')),int(input('Inserisci yp: '))))
    elif x==5:
        print('\nHai selezionato la funzione divisibile')
        if divisibile(int(input('Inserisci x: ')),int(input('Inserisci y: '))):
            print('x è divisibile per y')
        else:
            print('x non è divisibile per y')
    elif x==6:
        print('\nHai selezionato la funzione compreso_tra')
        if compreso_tra(int(input('Inserisci x: ')),int(input('Inserisci y: ')),int(input('Inserisci z: '))):
            print('y è compreso tra x e z')
        else:
            print('y non è compreso tra x e z')
    elif x==7:
        print('\nHai selezionato la funzione fattoriale')
        print('Il fattoriale è: ',fattoriale(int(input('Inserisci un numero: '))))

    else:
        print('Hai sbagliato qualcosa')
    y=input('\nVuoi continuare? [y/n]')
'''
    

print(funzioni)
funz = ['area(eval(input(\'Inserisci raggio: \')))','area1(int(input(\'Inserisci il raggio: \')))','valore_assoluto(int(input(\'Inserisci un valore: \')))',
        'distanza(int(input(\'Inserisci x1: \')),int(input(\'Inserisci y1: \')),int(input(\'Inserisci x2: \')),int(input(\'Inserisci y2: \')))','area_cerchio(int(input(\'Inserisci xc: \')),int(input(\'Inserisci yc: \')),int(input(\'Inserisci xp: \')),int(input(\'Inserisci yp: \')))',
        'divisibile(int(input(\'Inserisci x: \')),int(input(\'Inserisci y: \')))','compreso_tra(int(input(\'Inserisci x: \')),int(input(\'Inserisci y: \')),int(input(\'Inserisci z: \')))','fattoriale(int(input(\'Inserisci un numero: \')))']
r = input('Che funzione vuoi provare: ')
print(eval(eval('funz[{}]'.format(r))))


