import math
from functools import reduce

def triangle_num(num):
    iter = 0
    for number in range(1,num+1):
        iter += number

    return iter

def fac_lys(num):
    lyst1 = list(range(1, round(math.sqrt(num)+1)))
    factors = []
    for i in lyst1:
        if num%i == 0:
            answer = num/i
            factors.append(i)
    if num % 2 == 0:
        factors.append(num/2)
    factors.append(num)
    print(factors)
    return factors

def factors(n):
    return reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))


def count_facs(lyst):
    return len(lyst)

#generate triangle number
#calculate and count fac list
#if the fac list for  tri_num > 500 return number

num_factors = 0
number = 1

while num_factors < 500:
    x = triangle_num(number)
    num_factors = count_facs(factors(x))
    print("Tri_num:" + " "+ str(x))
    print("..."+ str(num_factors)+ "factors")

    number += 1

#print(len(fac_lys(842161320)))
############################
#Tri_num: 842161320
#...514 factors
