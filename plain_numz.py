

fir = 10000
sec = 998001


#check palindromality
def is_pal(num):
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False

###palindrome lyst maker
def palin_lys(x, y):
    lyst  = range(x, y)
    lyst2 = []

    for i in lyst:
        if is_pal(i) == True:
            lyst2.append(i)

    return lyst2

##Collects list of plaindrome factors from different numbers
def fac_lis(num):
    lyst = list(range(100, 999))
    lyst2 = []
    for i in lyst:
        mult = num/i
        if num % i == 0 and mult < 999:
            lyst2.append(mult)
            lyst2.append(i)
        
    return lyst2

def palin_fac(lyst):
    lol = []
    for num in lyst:
        lis = fac_lis(num)
        if len(lis) > 2:
            lol.append(lis)
    return lol


pals = palin_lys(fir, sec)
print(pals)
print(palin_fac(pals))
