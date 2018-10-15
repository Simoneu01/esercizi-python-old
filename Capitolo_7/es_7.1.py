import math

epsilon=0.000000000000001

def mia_radq(a):
    x = 3
    while True:
        y = (x + a/x) /2
        if abs(y-x) < epsilon:
            break
        x = y
    return x


def test_radq():
    print('a\tmia_radq(a)\t\tmath.sqrt(a)\t\tdiff')
    print('-\t-----------\t\t-----------\t\t-----')
    i=1
    while i<10:
        mia_radq(i)
        diff=abs(mia_radq(i)-math.sqrt(i))
        print(i,mia_radq(i),' '*(20 - len(math.sqrt(i))),' '*(20-len(diff)))
        i=i+1
        
test_radq()
