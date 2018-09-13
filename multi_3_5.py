def multi_3_5(num):
    one = 0
    two = 0
    three = 0
    lyst = []
    for i in range(num):
        if i%3 == 0 and i%5 == 0:
            lyst.append(i)
            one += i
        if i % 3 == 0 and i%5 != 0:
            lyst.append(i)
            two += 1
        elif i % 5 == 0 and i % 3 != 0:
            lyst.append(i)
            three += i

    fin = one + two + three
    print(lyst)
    return sum(lyst)

print(multi_3_5(1000))
