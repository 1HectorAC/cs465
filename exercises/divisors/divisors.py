import math
def divisors(num):
    divisors = []
    for x in range(1,int(num/2) + 1):
        if num % x == 0:
            divisors.append(x)
    divisors.append(num)
    return divisors