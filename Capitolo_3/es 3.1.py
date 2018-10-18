def giustifi_destra(s):
    i=0
    while i<=(70-len(s)):
        s =' '+s
        i+1
    print(s)

y='y'
while y!='n':
    giustifi_destra(input('Inserisci stringa: '))
    y=input('Vuoi continuare? [y/n]')

print('{:<20}'.format(input('INSERISCI UNA PAROLA: ')))
