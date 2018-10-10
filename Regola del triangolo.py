#In un triangolo ogni lato è minore della somma degli altri due lati.
#scrivere uno script Python, usando una funzione, in cui dati 3 numeri
#(che sono i lati) verifica se è un triangolo oppure no.

def triangolo(a,b,c):
    triangolo=True
    if a>(b+c):
        triangolo=False
    elif b>(a+c):
        triangolo=False
    elif c>(b+a):
        triangolo=False
        
    if triangolo is True:
        print('è un triangolo')
    else:
        print('Non è un triangolo')

y='y'
while y!='n':
    a=int(input('Inserisci il primo lato: '))
    b=int(input('Inserisci il secondo lato: '))
    c=int(input('Inserisci il terzo lato: '))
    triangolo(a,b,c)
    y=input('\nVuoi continuare [y/n]?')
 
