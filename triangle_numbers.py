import math
from functools import reduce

#generate triangle number
#calculate and count fac list
#if the fac list for  tri_num > 500 return number

def triangle_num(num):
    iter = 0
    for number in range(1,num+1):
        iter += number

    return iter


def factors(n):
    return reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))


def count_facs(lyst):
    return len(lyst)


num_factors = 0
number = 1

###########################################################
while num_factors < 500:
    x = triangle_num(number)
    num_factors = count_facs(factors(x))
    print("Tri_num:" + " "+ str(x))
    print("..."+ str(num_factors)+ "factors")

    number += 1
