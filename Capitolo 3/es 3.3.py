def fai2volte(f):
    f()
    f()

def fai4volte(f):
    fai2volte(f)
    fai2volte(f)

def print_striscia():
    print('+ - - - -', end=' ')

def print_spazio():
    print('|        ', end=' ')

def print_strisce():
    fai2volte(print_striscia)
    print('+')

def print_spazi():
    fai2volte(print_spazio)
    print('|')

def print_riga():
    print_strisce()
    fai4volte(print_spazi)

def print_griglia():
    fai2volte(print_riga)
    print_strisce()

print('Griglia 2x2')
print_griglia()
print('\nGriglia 4x4')
def print_striscia():
    print('+ - - - - + - - - -', end=' ')

def print_spazio():
    print('|         |        ', end=' ')

def print_griglia():
    fai4volte(print_riga)
    print_strisce()

print_griglia()
