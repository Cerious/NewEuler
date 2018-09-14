import math

##we can use a nested "for loop" to check a = 1..1000 against b = 2..1000
##this willl give us c^2. we will then get c and add it together with a&b
##if this adds togeher to give us 1000 then we will take those those three numbers
##and multiply them together to  yield our final answer
##we must also  be care ful that "a" does not exceeed "b"
#perhaps we shoudl make these 3 numbers into lists of legth 3 lists

def pytrip_gen(aran, bran):
    lys = []
    for a in aran:
        for b in bran:
            c_sqrd = a**2 + b**2
            c = math.sqrt(c_sqrd)
            lys.append([a,b,c])
    return lys


a_ran = range(1,1001)
b_ran = range(1,1001)

def sum_em_up(aran, bran):
    pyts = pytrip_gen(aran, bran)
    lys = []
    for i in pyts:
        lys.append(sum(i))
    return lys

def include(num, lys):
    bool = False
    for i in lys:
        if i == num:
            bool = True
        else:
            pass
    return bool

lys = sum_em_up(a_ran, b_ran)
print(include(1000, lys))
print(lys.index(1000))
pyts = pytrip_gen(a_ran, b_ran)
z = pyts[199374]

prod = 1
for value in z:
    print(prod)
    prod*= value

print("Final product: " + str(prod))
