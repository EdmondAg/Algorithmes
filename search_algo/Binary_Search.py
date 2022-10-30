# from Util import generate_list
#
#
# l = generate_list(20,-20,20)
# print(l)


def search(l, e, imin, imax):
    if imax - imin == 0:
        if l[imin] == e:
            return imin
        return -1
    if imax - imin == 1:
        if l[imin] == e:
            return imin
        if l[imax] == e:
            return imax
        return -1
    icenter = (imax + imin) // 2
    if l[icenter] == e:
        return icenter
    if l[icenter] < e:
        return search(l, e, icenter + 1, imax)
    return search(l, e, imin, icenter - 1)


def binary_search(l, e):
    length = len(l)-1
    return search(l, e, 0, length)


l = [1, 4, 6, 11, 12, 16, 20, 20, 22, 24, 25, 30, 33, 40]
l.sort()

print(binary_search(l, 33))
