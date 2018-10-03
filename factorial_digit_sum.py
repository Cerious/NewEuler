###########################################################
##Find the sum of the digits in the number 100!##
###########################################################
import helpful_math

def factorial(number):
    life = list(range(2, number+1))
    final = helpful_math.times_list(life)
    return final

def replace(lyst, element, repli, index):
    x = lyst.index(element)
    lyst.pop(index)
    lyst.insert(index, repli)
    return lyst

def digit_add(digit):

    life = list(str(digit))
    lyst = []
    index = 0
    for i in life:
        replace(life, life[index], int(life[index]), index)
        index += 1

    return sum(life)


x = digit_add(factorial(100))
print(x)

##Answer: 648