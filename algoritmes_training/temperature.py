import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = [5526]  # the number of temperatures to analyse
minP = 5526
minN = -273
minT = 0  # t: a temperature expressed as an integer ranging from -273 to 5526
for i in n:
    t = int(i)
    if len(n) >= 1:
        if minP > t > 0:
            minP = t
            minT = minP
        if minN < t < 0:
            minN = t
            minT = minN
        if -minP == minN:
            minT = minP
        elif -minP > minN:
            minT = minP
        elif -minP < minN:
            minT = minN
    elif len(n) is None or n == 0:
        minT = 0
    elif len(n) == 1:
        minT=t

print(minT)
