# Calculate power of a number

'''
Assumptions : Number can be any integer ( postive, negative or Zero)

x^n = x * X^n-1

'''

def power_of_num ( base, power_times):
    
    assert power_times >= 0 and int(power_times) == power_times,"Power of a number has to be positive integer"
    if power_times == 1:
        return base
    return base * power_of_num(base, power_times-1)

print(power_of_num(-5,4))