#987
big_num = int(7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215533697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450)

big_str = str(big_num)
print(big_num)
print(len(big_str))
print(big_str[987])
strg = 'x'*10


def splitter(num, strn):
    place = 0
    lys = []
    for i in strn:
            lys.append(list(strn[place:place+num]))
            place += 1

    return lys


lys = splitter(13, big_str)
lys2 = []
for i in lys:
    lys3 = []
    for j in i:
        lys3.append(int(j))
    lys2.append(lys3)




print(strg)
print(len(lys2))
fin = lys2[0:985]
print(fin)
print(len(fin[-1]))

final = []

for i in fin:
    prod = 1
    for j in i:
        prod *= j
    final.append(prod)

print(final)
print(max(final))
