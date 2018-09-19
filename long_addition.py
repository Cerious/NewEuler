from functools import reduce

op = open('one_fiddy.txt', 'r')
lyst = op.read().splitlines()
op.close()
lyst.pop(0)
lyst.pop(-1)
print(lyst)
print('########################################################')
for i in lyst:
    print(len(i))

print('##################################################################')
int_lyst = []
for num in lyst:
    int_lyst.append(int(num))
missing = 37107287533902102798797998220837590246510135740250
int_lyst.insert(0, missing)
print(len(int_lyst))
print(int_lyst)
lyst2=[]
lyst2.append(reduce(lambda x, y: x+y,  int_lyst))
print(lyst2[0])

for i in lyst2:
    print("First Ten")
    x = str(i)
    y = x[0:10]
    z = str(y)
    print(y)
    print(len(z))
