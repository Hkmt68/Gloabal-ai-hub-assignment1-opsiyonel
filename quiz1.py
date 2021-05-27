odd = [1,3,5,7,9]
even = [0,2,4,6,8]
newList = [allNum * 2 for allNum in odd + even]

for allNum in newList:
    print(type(newList))

