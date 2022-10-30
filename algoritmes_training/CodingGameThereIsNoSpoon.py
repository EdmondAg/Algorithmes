import sys
import math

# Don't let the machines win. You are humanity's last hope...

w = int(input())  # the number of cells on the X axis
h = int(input())  # the number of cells on the Y axis
line = []
for i in range(h):
    line.append(input())  # width characters, each either 0 or .

for y in range(h):
    for x in range(w):
        y2 = -1
        x2 = -1
        y3 = -1
        x3 = -1
        if line[y][x] == "0":
            if x < w - 1:
                for xs in range(x + 1, w):
                    if line[y][xs] == "0":
                        x2 = xs
                        y2 = y
                        break
            if y < h - 1:
                for ys in range(y + 1, h):
                    if line[ys][x] == "0":
                        x3 = x
                        y3 = ys
                        break
            print(x, y, x2, y2, x3, y3)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


# Three coordinates: a node, its right neighbor, its bottom neighbor
