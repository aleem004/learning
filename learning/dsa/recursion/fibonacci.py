# Fibanacci : sequence on number each number is sum of previous 2 numbers and sequence starts from 0 and 1

# Question : check if the given number in FIbonacci number 

# Assumptions : 

'''
1. Steps : Define recursive case :

        f(n) = f(n-1) + f(n-2)

'''

def fibonacci(n):
    assert n>=0 and int(n)==n, "Number has to be postive integer and non-integer"

    if n in [0, 1 ] :
        return n

    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(-1))


