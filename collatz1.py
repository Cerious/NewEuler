import operator

def gen_coll_seq(starter_number):
    x = starter_number
    final = [starter_number]
    while x >= 1:
        if x%2 == 0:
            x = x/2
            final.append(x)
        elif x == 1:
            x = 0
        elif x%2 != 0:
            x = (3*x) + 1
            final.append(x)

    return final

def coll_seqz(top_number):
    demi_lys = list(range(1,top_number))
    actual_lys = list(reversed(demi_lys))
    collatz_dict = {}
    for i in actual_lys:
        #generate the collatz seq & #count the length of the list
        #append the k:v pair to collatz_dict
        collatz_dict.update({i : len(gen_coll_seq(i))})

    return collatz_dict


def greatest_coll_seq(dictionary):
     return max(dictionary.items(), key=operator.itemgetter(1))[0]

#herez the anwser
print(greatest_coll_seq(coll_seqz(1000001)))
