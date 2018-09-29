#model 20x20 grid as 441 points
from typing import List, Any


def make_grid():
    lyst = []
    a = 1
    b = 22
    for i in range(1, 22):
        ly = []
        for num in range(a, b):
            ly.append(num)

        lyst.append(ly)
        a = a+21
        b = b+21

    return lyst

def get_neighbors(lol, node):
    return None
def neighbors(list_of_lists):
    neighborz = {}
    for lyst in list_of_lists:

        for i in lyst:
            dict.update()

def permutations(dir1, dir2, dim1, dim2):
    direction1 = dir1*dim1
    direction2 = dir2*dim2

    union = list(direction1 + direction2)

    return union

print(permutations('r', 'd', 20, 20))


