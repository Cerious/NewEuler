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
    index_i = 0
    for i in lyst:
        index_j = 0
        for j in i:
            temp_lys = []
            if index_j < 17 and index_i < 17:
                temp_lys.append(j)
                temp_lys.append(lyst[index_i+1][index_j+1])
                temp_lys.append(lyst[index_i+2][index_j+2])
                temp_lys.append(lyst[index_i+3][index_j+3])
                final_lys.append(temp_lys[:])
                temp_lys.clear()
            else:
                pass
            index_j += 1
        index_i += 1
    return final_lys

def get_diag_rev(lyst):
    final_lys = []
    index_i = 0
    for i in lyst:
        index_j = 0
        for j in i:
            temp_lys = []
            if index_j > 2 and index_i < 17:
                temp_lys.append(j)
                temp_lys.append(lyst[index_i+1][index_j-1])
                temp_lys.append(lyst[index_i+2][index_j-2])
                temp_lys.append(lyst[index_i+3][index_j-3])
                final_lys.append(temp_lys[:])
                temp_lys.clear()
            else:
                pass
            index_j += 1
        index_i += 1
    return final_lys


def get_hor(lyst):
    final_lys = []
    index_i = 0
    for i in lyst:
        index_j = 0
        for j in i:
            temp_lys = []
            if index_j < 17:
                temp_lys.append(j)
                temp_lys.append(lyst[index_i][index_j+1])
                temp_lys.append(lyst[index_i][index_j+2])
                temp_lys.append(lyst[index_i][index_j+3])
                final_lys.append(temp_lys[:])
                temp_lys.clear()
            else:
                pass
            index_j += 1
        index_i += 1
    return final_lys




def get_ver(lyst):
    #Need to change rules
    final_lys = []
    index_i = 0
    for i in lyst:
        index_j = 0
        for j in i:
            temp_lys = []
            if index_i < 17:
                temp_lys.append(j)
                temp_lys.append(lyst[index_i+1][index_j])
                temp_lys.append(lyst[index_i+2][index_j])
                temp_lys.append(lyst[index_i+3][index_j])
                final_lys.append(temp_lys[:])
                temp_lys.clear()
            else:
                pass
            index_j += 1
        index_i += 1
    return final_lys

def lol_scan(lol):
    reg_list = []
    for i in lol:
        reg_list.append(reduce(lambda x, y: x*y,  i))
    return max(reg_list)

def lol_scan_test(lol):
    reg_list = []
    for i in lol:
        reg_list.append(reduce(lambda x, y: x*y,  i))
    return reg_list

def rev_list(ly_of_ly):
    nu_lys = []

    for i in ly_of_ly:
        nu_lys.append(list(reversed(i)))

    final_lys = list(reversed(nu_lys))
    return final_lys

rev = rev_list(list_of_list)


ver = get_ver(list_of_list)
hor = get_hor(list_of_list)
diag = get_diag(list_of_list)
rev_diag = get_diag_rev(list_of_list)

final = []
final.append(lol_scan(hor))
final.append(lol_scan(ver))
final.append(lol_scan(diag))
final.append(lol_scan(rev_diag))
print(final)
print(max(final))

print(diag)
diag2 = lol_scan_test(diag)

print(1788696 in diag2)

iter = 0
for i in diag:
    iter += 1
    print(str(iter) + ":"+ " "+ str(i))

#print(lol_scan(rev_diag))
