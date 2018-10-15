def fai2volte(f, a):
    f(a)
    f(a)

def stampa_2volte(a):
    print(a)
    print(a)

def fai4volte(f, a):
    fai2volte(f, a)
    fai2volte(f, a)
    
y='y'
while y!='n':
    fai2volte(stampa_2volte, 'spam')
    print('')
    fai4volte(stampa_2volte, 'spam')
    y=input('\nVuoi continuare? [y/n]')
    

