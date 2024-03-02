import random, sys, time, copy

ENI = 10
BIIKTIGI = 5

TIRI = '*'
OLI = ' '

kelesiUrpaqUiashyqtary = {}
for x in range(ENI):
    for y in range(BIIKTIGI):
        if random.randint(0, 1) == 0:
            kelesiUrpaqUiashyqtary[(x, y)] = TIRI
        else:
            kelesiUrpaqUiashyqtary[(x, y)] = OLI

print(kelesiUrpaqUiashyqtary)
