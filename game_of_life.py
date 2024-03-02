import copy, random, sys, time

ENI = 10
BIIKTIGI = 5

TIRI = '*'
OLI = ' '

kelesiUiashyqtar = {}
for x in range(ENI):
    for y in range(BIIKTIGI):
        if random.randint(0, 1) == 0:
            kelesiUiashyqtar[(x, y)] = TIRI
        else:
            kelesiUiashyqtar[(x, y)] = OLI

while True:
    print('\n' * 10)
    uiashyqtar = copy.deepcopy(kelesiUiashyqtar)

    for y in range(BIIKTIGI):
        for x in range(ENI):
            print(uiashyqtar[(x, y)], end='')
        print()
    print('Шығу үшін Ctrl-C пернесін басыңыз')

    for x in range(ENI):
        for y in range(BIIKTIGI):
            sol = (x - 1) % ENI
            on = (x + 1) % ENI
            jogargy = (y - 1) % BIIKTIGI
            tomengi = (y + 1) % BIIKTIGI

            korshilerSany = 0
            if uiashyqtar[(sol, jogargy)] == TIRI:
                korshilerSany += 1
            if uiashyqtar[(x, jogargy)] == TIRI:
                korshilerSany += 1
            if uiashyqtar[(on, jogargy)] == TIRI:
                korshilerSany += 1
            if uiashyqtar[(sol, y)] == TIRI:
                korshilerSany += 1
            if uiashyqtar[(on,  y)] == TIRI:
                korshilerSany += 1
            if uiashyqtar[(sol, tomengi)] == TIRI:
                korshilerSany += 1
            if uiashyqtar[(x, tomengi)] == TIRI:
                korshilerSany += 1
            if uiashyqtar[(on, tomengi)] == TIRI:
                korshilerSany += 1

            if uiashyqtar[(x, y)] == TIRI and (korshilerSany == 2 or
                                               korshilerSany == 3):
                kelesiUiashyqtar[(x, y)] = TIRI
            elif uiashyqtar[(x, y)] == OLI and korshilerSany == 3:
                kelesiUiashyqtar[(x, y)] = TIRI
            else:
                kelesiUiashyqtar[(x, y)] = OLI

    try:
        time.sleep(2)
    except KeyboardInterrupt:
        print('Conways Game of Life')
        sys.exit()

