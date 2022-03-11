# Sum of positive numbers

# Add sum of all positive number

### f(n) = n%10 + f(n)/10

#Assumptions :
    # Number is a positive in


def sum_of_digit(n):

    assert n >= 0 and int(n) == n, "Number has to be positive Integer"
    if n == 0:
        return 0;

    return n%10 + sum_of_digit(n/10)


print(sum_of_digit(541))

