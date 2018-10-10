#chiedere l'età di uno studente e dire se è maggiorenne o minorenne.
#Se maggiorenne elencare i suoi diritti (es. votare, patente, ecc.)

diritti="""

Secondo l'ordinamento italiano, con la maggiore età si acquisisce:
- la capacità di agire, da non confondere con la capacità giuridica
- La maggiore età è fissata al compimento del diciottesimo anno dal diritto romano.
- L'articolo 48 della Costituzione attribuisce il diritto di voto ai cittadini maggiorenni
- Infine, è un puro caso se l'età minima per il conseguimento della patente di guida europea di categoria B in Italia coincida con la maggiore età:
  per il conseguimento della patente di categoria A1 bastano 16 anni, mentre per categorie superiori ne sono necessari sino a 24.
"""
def età(a):
    if a>=18:
        print('Lo studente è maggiorenne',diritti)
    else:
        print('Lo studente non è maggorenne')

y='y'
while y!='n':
    a=int(input("Inserisci l'età dello sudente: "))
    età(a)
    y=input('\nVuoi continuare [y/n]?')
 
