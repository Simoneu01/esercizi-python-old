'''
Esercizio 6.4. Un numero, a, è una potenza di b se è divisibile per b e a/b è a sua volta una potenza
di b. Scrivete una funzione di nome potenza che prenda come parametri a e b e che restituisca True
se a è una potenza di b. Nota: dovete pensare bene al caso base.
'''

def potenza (a,b):
    while a % b == 0:  #Finchè a è divisibile per b 
        a = a / b	   #allora imposta a=a/b
    if a == 1:		   #se a è 1 
        return True    #allora a è una potenza di b ritorna "True"
    return False	   #se a non è una potenza di b ritorna "False"

y='y'
while y!='n':
    a=int(input('Inserisci a: '))
    b=int(input('Inserisci b: '))
    if (potenza(a,b)== True):
        print(a,'è una potenza di',b)
    else:
        print(a,'non è una potenza di',b)
    y=input('\nVuoi continuare? [y/n]')
