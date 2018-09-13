import math

def rm_even(lyst):
    for i in lyst:
        if i % 2 == 0 and i != 2:
            lyst.pop(lyst.index(i))
    return lyst

def is_prime(num):
    lyst =  list(range(2, round(math.sqrt(num)+1)))
    count = 0
    bool = None
    for i in lyst:
        if num % i == 0:
            count += 1
        elif num % i != 0:
            bool = True

    if count > 0:
        bool = False

    return bool




def prime_lys(num):
    print("output1")
    lyst1 = list(range(2,round(math.sqrt(num)+1)))
    #print(round(math.sqrt(num)+1))
    #print(lyst1)
    nu_lyst = rm_even(lyst1)
    thrd = []
    #print(nu_lyst)
    for i in nu_lyst:
        if num % i == 0:
            thrd.append(i)
    prm = []
    #print("multiples:")
    #print(thrd)
    for i in thrd:
        if is_prime(i) == True:
            prm.append(i)
    print(prm)
    return prm

#x = prime_lys(600851475143)
#print(x[-1])
