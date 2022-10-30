import random


def generate_list(n, min, max):
    list = []
    for i in range(n):
        e = random.randint(min, max)
        list.append(e)
    return list


def quicksort(list):
    qsort_loop(list, 0, len(list) - 1)


def qsort_loop(list, iMin, iMax):
    if iMax - iMin == 1:
        if list[iMin] > list[iMax]:
            list[iMin], list[iMax] = list[iMax], list[iMin]
        return
    if iMax - iMin == 0:
        return

    p = list[iMax]
    a = 0

    for i in range(iMin, iMax):
        if list[i] <= p:
            list[a + iMin], list[i] = list[i], list[a + iMin]
            a += 1
    list[a + iMin], list[iMax] = p, list[a + iMin]
    if a != 0:
        qsort_loop(list, iMin, a + iMin - 1)
    if iMax > a + iMin + 1:
        qsort_loop(list, a + iMin + 1, iMax)


def check_ordered(l):
    for i in range(len(l) - 1):
        if l[i + 1] < l[i]:
            return False
    return True


l = generate_list(90, -1000, 1000)
print("unsorted:", l)
quicksort(l)
print("sorted:  ", l)

