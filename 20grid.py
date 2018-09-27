#model 20x20 grid as 441 points
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