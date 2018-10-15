'''
dato un numero maggiore di 5 scrivere una funzione in Python che definisce se il numero dato è primo
ricordarsi che:
- un numero primo non è pari (quindi il resto della divisione per 2 è diverso da zero)
- un numero primo è primo se i suoi divisori sono 1 e sè stesso
- un numero primo (maggiore di 5) è dispari
'''

def primo(numero):
    primo=True
    l = int(numero ** 0.5)+1
    for n in range(2, l):       
        if numero % n == 0:
            primo=False        
    if primo == True:
        print('è un numero primo')
    elif primo == False:
        print('non è un numero primo')


y='y'
while y!='n':
    primo(int(input('Inserisci un numero: ')))
    y=input('\nVuoi continuare [y/n]?')
