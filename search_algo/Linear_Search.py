from Util import generate_list


def linear_search(l, e):
    for i in range(len(l)):
        if e == l[i]:
            return i
    return -1


l = generate_list(200,-20,200)


print(linear_search(l, 1)
)