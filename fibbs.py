def fibs(numb):
    num = 0
    arr = [1,2]
    while num <= numb:
        num = arr[-1] + arr[-2]
        if num <= numb:
            arr.append(num)

    return arr
def even_fibs(lyst):
    arr = []
    for i in lyst:
        if i%2 ==0:
            arr.append(i)
    print(arr)
    return sum(arr)

print(fibs(4000000))
print(even_fibs(fibs(4000000)))
