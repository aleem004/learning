"""
Question : Convert a number from Decimal to binary

Function :

    f(x) = f(x)/2 + (x%2)*10 + x

Ex:
15 Remainder Quotient

15/2    6   1
6       3   0
3       1   1
1       0   1

"""


def decimal_to_binary(n):

    assert int(n)==n,"Parameter must be an integer"

    if n ==0 :
        return 0
    return n%2 + 10 * decimal_to_binary(int(n/2))


print(decimal_to_binary(16))