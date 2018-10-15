#
#
#

def contoallarovescia(n):
    if n <= 0:
        print('Via!')
    else:
        print(n)
        contoallarovescia(n-1)

contoallarovescia(5)
