
def prod_sum(number):
    str_num = str(number)
    iter = 0
    for i in str_num:
        iter += int(i)

    return iter

big_number = 2**1000
print(prod_sum(big_number))
