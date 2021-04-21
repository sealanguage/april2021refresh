

aList = [3, 1, 4, 2, 7]
bList = [8, 2, 5, 4, 6]

aList = [1, 2, 3, 4, 7, 9, 12, 6, 15, 20, 11, 18, 5, ]
bList = [3, 6, 7, 8, 12, 11, 31, 24, 20, 18]


iterations = []

aList.sort()
bList.sort()

print(aList)
print(bList)

for anum in aList:
    for bnum in bList:
        if anum < bnum:
            pass
        elif anum == bnum:
            iterations.append(anum)

print(iterations)

