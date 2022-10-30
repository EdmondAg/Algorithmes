def longest_and_shortest_word(sentence):
    # long way
    words = sentence.split(" ")
    shortestDef = words[1]
    longestDef = words[1]
    for w in words:
        if len(w) > len(longestDef):
            longestDef = w
        if len(w) < len(shortestDef):
            shortestDef = w
    return shortestDef, longestDef


def long_short_word(sentence):
    # short way
    words = sentence.split(" ")
    maxW = max(words, key=len)
    minW = min(words, key=len)
    return minW, maxW


def long_short_word_alpha(s):
    shortest, longest = long_short_word(s)
    words = s.split(" ")
    minWlist = []
    maxWlist = []
    for w in words:
        if len(w) == len(shortest):
            minWlist.append(w)
        if len(w) == len(longest):
            maxWlist.append(w)
    minWlist.sort()
    maxWlist.sort()
    return minWlist[0], maxWlist[0]


s = "Un chasseur sachant chasser sait chasser  sans chien"

shortest, longest = long_short_word_alpha(s)

print(shortest)
print(longest)
