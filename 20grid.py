##make function that determines the number of move combinations from
##point a to point b in an AxB grid
##determine the number and direction of moves from path to goal.

import helpful_math

def combinations(dir1, dir2, dim1, dim2):
    direction1 = dir1*dim1
    direction2 = dir2*dim2

    abstract = dim1 + dim2
    rev = abstract - dim1
    rev2 = abstract - dim2
    daLyst = list(range(rev+1, abstract+1))
    print(daLyst)
    possibl = helpful_math.times_list(daLyst)
    daLyst2 = list(range(1, rev2+1))
    print(daLyst2)
    redun = helpful_math.times_list(daLyst2)

    final  =  possibl/redun
    return final


print(combinations('r', 'd', 20, 20))


