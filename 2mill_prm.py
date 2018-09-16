import math


def rm_even(lyst):
    for i in lyst:
        if i % 2 == 0 and i != 2:
            lyst


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

def prm_lys(num):
    ran = range(2,num)
    ran2 = rm_even(ran)
    lys = []
    for i in ran:
        if is_prime(i) == True:
            lys.append(i)
            print("Prime # " +str(lys.index(i)+1)+":"+" "+str(lys[-1]))

    return lys


x = prm_lys(2000000)
print(len(x))

print(sum(x)+2)
