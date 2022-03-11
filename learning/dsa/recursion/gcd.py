'''
Question : Calculate largest greatest common divisor of a number.

Euclidan Algorithm :



'''

def gcd(a,b):

    assert  int(a) == a and int(b) == b,"Numbers hsould be integers"
    if b == 0:
        return a
    else:
        return gcd(b,a % b)


print(gcd(18,48))