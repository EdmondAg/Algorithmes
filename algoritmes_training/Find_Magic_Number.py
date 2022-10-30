import random

# REUSSITE IMPORTANTE J'ai reussi a faire ca en solo
MIN_NR = 0
MAX_NR = 100
number = random.randint(MIN_NR, MAX_NR)
print("Magic:", end="")
print(number)


def read_answer(n):
    if n == number:
        print("Bravo")
        return 0
    if n > number:
        print("Magic is smaller")
        return -1
    elif n < number:
        print("Magic is bigger")
        return 1


def ai_search_number(init_nr, newMin=0, newMax=0):
    answer = read_answer(init_nr)
    if answer == 0:
        return init_nr

    if answer == -1:
        newMax = init_nr
        init_nr //= 2
        if init_nr <= newMin:
            init_nr = (newMin + newMax) // 2
        return ai_search_number(init_nr, newMin, newMax)

    if answer == 1:
        newMin = init_nr
        init_nr *= 2
        if init_nr >= newMax:
            init_nr = (newMin + newMax) // 2
        return ai_search_number(init_nr, newMin, newMax)


print("AI: " + str(ai_search_number(5, MIN_NR, MAX_NR)), end="")
