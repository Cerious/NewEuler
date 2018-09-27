from num2words import num2words


def num_word_adder(num):
    iterator = 0
    for i in range(1, num+1):
        strg = num2words(i)
        x = strg.replace(' ', '')
        x = x.replace('-', '')
        iterator += len(x)

    return iterator

print(num_word_adder(1000))
