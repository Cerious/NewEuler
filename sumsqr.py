def sqr_sum(num):
    ran = range(1,num+1)
    iter = 0
    for i in ran:
        iter += (i**2)

    return iter
def sum_sqr(num):
    ran = range(1, num+1)
    iter = 0
    for i in ran:
        iter += i

    x = iter**2
    return x
def diff(num):
    diffy = sum_sqr(num) - sqr_sum(num)
    return diffy


print(sum_sqr(10))
print(sqr_sum(10))
print(diff(100))
