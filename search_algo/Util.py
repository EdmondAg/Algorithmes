import random


def generate_list(n, min, max):
    list = []
    for i in range(n):
        e = random.randint(min, max)
        list.append(e)
    return list

