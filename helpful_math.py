from functools import reduce

def factors(n):
    return reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))






def times_list(lyst):
    x = reduce(lambda x, y: x*y, lyst)

    return x


print(times_list([2,2,2]))