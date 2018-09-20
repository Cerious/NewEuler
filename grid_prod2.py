from functools import reduce

open = open('grid.txt', 'r')
lyst = open.read().splitlines()
open.close()


fir = '08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08'
lyst.pop(0)
lyst.insert(0, fir)


list_of_list = []

for i in lyst:
    list_of_list.append(i.split(" "))

print(list_of_list)

for i in list_of_list:
    print(len(i))

def replace(lyst, element, repli, index):
    x = lyst.index(element)
    lyst.pop(index)
    lyst.insert(index, repli)
    return lyst

print('####################################')
fir_lyst = fir.split(" ")
print(fir_lyst)
replace(fir_lyst,fir_lyst[0] ,int(fir_lyst[0]), 0)
print(fir_lyst)

#use the replace method to replace all string numbers with integer numbers
for i in list_of_list:
    for j in i:
        replace(i, j, int(j), i.index(j))

#flatten list of numbers
def flatten(lol):
    final = []
    for i in lol:
        for j in i:
            final.append(j)
    return final

numbers = flatten(list_of_list)


def get_diag(lyst):
    final_lys = []
    for i in lyst:
        for j in i:
            temp_lys = []
            if i.index(j) < 17 and lyst.index(i) < 17:
                temp_lys.append(j)
                temp_lys.append(lyst[lyst.index(i)+1][i.index(j)+1])
                temp_lys.append(lyst[lyst.index(i)+2][i.index(j)+2])
                temp_lys.append(lyst[lyst.index(i)+3][i.index(j)+3])
                final_lys.append(temp_lys[:])
                temp_lys.clear()
    return final_lys


def get_hor(lyst):
    final_lys = []
    for i in lyst:
        for j in i:
            temp_lys = []
            if i.index(j) < 17:
                temp_lys.append(j)
                temp_lys.append(lyst[lyst.index(i)][i.index(j)+1])
                temp_lys.append(lyst[lyst.index(i)][i.index(j)+2])
                temp_lys.append(lyst[lyst.index(i)][i.index(j)+3])
                final_lys.append(temp_lys[:])
                temp_lys.clear()
    return final_lys




def get_ver(lyst):
    #Need to change rules
    final_lys = []
    for i in lyst:
        for j in i:
            temp_lys = []
            if lyst.index(i) < 17:
                temp_lys.append(j)
                temp_lys.append(lyst[lyst.index(i)+1][i.index(j)])
                temp_lys.append(lyst[lyst.index(i)+2][i.index(j)])
                temp_lys.append(lyst[lyst.index(i)+3][i.index(j)])
                final_lys.append(temp_lys[:])
                temp_lys.clear()
    return final_lys

def lol_scan(lol):
    reg_list = []
    for i in lol:
        reg_list.append(reduce(lambda x, y: x*y,  i))
    return max(reg_list)

ver = get_ver(list_of_list)
hor = get_hor(list_of_list)
diag = get_diag(list_of_list)

final = []
final.append(lol_scan(hor))
final.append(lol_scan(ver))
final.append(lol_scan(diag))
print(final)
print(max(final))
