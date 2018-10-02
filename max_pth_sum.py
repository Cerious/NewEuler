file = open('tri_tree.txt', 'r')
head, *tri_str = file.read().splitlines()
file.close()
tri_str.insert(0, head[-2:])


def strs_to_lyst(str_list):
    liist = []
    for i in str_list:
        liist.append(list(i))

    return liist

def liststr_listlist(ly_str):
    life = []
    for i in ly_str:
        life.append(i.split(" "))
    return life

def replace(lyst, element, repli, index):
    x = lyst.index(element)
    lyst.pop(index)
    lyst.insert(index, repli)
    return lyst

def str_num_conv(list_of_lists):
    for i in list_of_lists:
        for j in i:
            replace(i, j, int(j), i.index(j))

    return list_of_lists


def getNeighbors(lyst, i, j):
    life = [lyst[i+1][j], lyst[i+1][j+1]]
    return life

def genNeighbors(list_of_list):
    dict = {}
    index_i = 0
    num = 0
    for i in list_of_list:
        index_j = 0
        for j in i:
            if index_i < 14:
                jay = str(j)+'-'+str(num)
                dict.update({jay: getNeighbors(list_of_list, index_i, index_j)})
            else:
                pass
            num += 1
            index_j += 1
        index_i += 1
    return  dict


lol = liststr_listlist(tri_str)
print(len(lol))
tri_list = str_num_conv(lol)
map = genNeighbors(tri_list)


print(map)

