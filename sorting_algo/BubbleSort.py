from random import randrange


def bubbleSort(listToSort):
    permutation = 1
    while permutation != 0:
        permutation = 0
        for i in range(len(listToSort) - 1):
            if listToSort[i] > listToSort[i + 1]:
                listToSort[i], listToSort[i + 1] = listToSort[i + 1], listToSort[i]
                permutation += 1


listInt = []
n = randrange(999)
for i in range(0, n):
    n2 = randrange(100)
    listInt.append(n2)

print(listInt)
bubbleSort(listInt)
print(listInt)
