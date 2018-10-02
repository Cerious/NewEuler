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

def leftNeighbors(lyst, i, j):
    life = [lyst[i][j], lyst[i+1][j], lyst[i+2][j], lyst[i+3][j]]
    return life

def rightNeihgbors(lyst, i,  j):
    life = [lyst[i][j], lyst[i+1][j+1], lyst[i+2][j+2], lyst[i+3][j+3]]
    return life

def getNeighbors(lyst, i, j):
    life = [lyst[i+1][j], lyst[i+1][j+1]]
    return life

def genNeighbors(list_of_list):
    left = []
    right = []

    index_i = 0
    num = 0
    for i in list_of_list:
        index_j = 0
        for j in i:
            if index_i < 12:
                left.append(leftNeighbors(list_of_list, index_i, index_j))
                right.append(rightNeihgbors(list_of_list, index_i, index_j))
            else:
                pass
            num += 1
            index_j += 1
        index_i += 1
    print(right)
    print(left)

def left_paths(dictionary):
    #i want to append the 4 downward neighbors to the list
    lyst = []
    addy = None
    for i in range(0, 4):
        #append addy
        return None
        #set addy to the left neigh of addy


def right_paths(dictionary):
    return None

i=0
j=0
lol = liststr_listlist(tri_str)
tri_list = str_num_conv(lol)
map = genNeighbors(tri_list)


print(map)

