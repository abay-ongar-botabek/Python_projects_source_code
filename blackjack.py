import random, sys

JUREK = chr(9829)
QIYQ = chr(9830)
QARGA = chr(9824)
SHYBYN = chr(9827)

KARTA_ARTY = 'backside'

def main():
    aqsha = 5000
    while True: 
        if aqsha <= 0:
            print("Сіздің қаражатыңыз бітті!")
            print("Құмар ойынды шын өмірде ойнамаңыз!")
            print("Ойын үшін рахмет!")
            sys.exit()
        print('Сіздің қаражатыңыз:', aqsha)
        stavka = stavkanyQabyldau(aqsha)

        koloda = kartaKolodasy()
        dilerQoly = [koloda.pop(), koloda.pop()]
        oiynshyQoly = [koloda.pop(), koloda.pop()]

        print('Сіз тіккен ақша:', stavka)
        while True:
            qoldyKorsetu(oiynshyQoly, dilerQoly, False)
            print()

            if qolUpaiynAlu(oiynshyQoly) > 21:
                break

            juris = juristiAlu(oiynshyQoly, aqsha - stavka)

            if juris == 'D':
                qosyumshaTigis = stavkanyQabyldau(min(stavka, (aqsha - stavka)))
                stavka += qosyumshaTigis
                print(f'Тігіс {stavka} ұлғайтылады')
                print('Тігіс:', stavka)

            if juris in ('H', 'D'):
                janaKarta = koloda.pop()
                rank, mast = janaKarta
                print(f'Сіз алған карта {rank} {mast}')
                oiynshyQoly.append(janaKarta)

                if qolUpaiynAlu(oiynshyQoly) > 21:
                    continue

            if juris in ('S', 'D'):
                break

        if qolUpaiynAlu(oiynshyQoly) <= 21:
            while qolUpaiynAlu(dilerQoly) < 17:
                print('Дилер карта алды ...')
                dilerQoly.append(koloda.pop())
                qoldyKorsetu(oiynshyQoly, dilerQoly, False)

                if qolUpaiynAlu(dilerQoly) > 21:
                    break
                input('Жалғастыру үшін Enter пернесін басыңыз...')
                print('\n\n')

        qoldyKorsetu(oiynshyQoly, dilerQoly, True)

        oiynshyUpaiy = qolUpaiynAlu(oiynshyQoly)
        dilerUpaiy = qolUpaiynAlu(dilerQoly)

        if dilerUpaiy > 21:
            print(f'Дилер асып кетті. Сіз {stavka}$ ұтып алдыңыз')
            aqsha += stavka
        elif (oiynshyUpaiy > 21) or (oiynshyUpaiy < dilerUpaiy):
            print('Сіз ұтылдыңыз.')
            aqsha -= stavka
        elif oiynshyUpaiy > dilerUpaiy:
            print(f'Сіз {stavka}$ ұтып алдыңыз')
            aqsha += stavka
        elif oiynshyUpaiy == dilerUpaiy:
            print("Тең болды. Тіккен ақшаңыз сізге қайтарылады")

        input('Жалғастыру үшін Enter пернесін басыңыз...')
        print('\n\n')


def stavkanyQabyldau(maxTigis):
    while True:
        print(f'Неше ақша тігіске қоясыз? (1-{maxTigis}, немесе QUIT)')
        stavka = input('> ').upper().strip()
        if stavka == 'QUIT':
            print('Ойын үшін рахмет')
            sys.exit()

        if not stavka.isdecimal():
            continue

        stavka = int(stavka)
        if 1 <= stavka <= maxTigis:
            return stavka
        

def kartaKolodasy():
    koloda = []
    for mast in (JUREK, QIYQ, QARGA, SHYBYN):
        for rank in range(2, 11):
            koloda.append((str(rank), mast))
        for rank in ('V', 'D', 'K', 'T'):
            koloda.append((rank, mast))
    random.shuffle(koloda)
    return koloda

def qoldyKorsetu(oiynshyQoly, dilerQoly, dilerQolynKorsetu):
    print()
    if dilerQolynKorsetu:
        print('ДИЛЕР:', qolUpaiynAlu(dilerQoly))
        kartalardyKorsetu(dilerQoly)
    else:
        print('ДИЛЕР: ???')
        kartalardyKorsetu([KARTA_ARTY] + dilerQoly[1:])

    print('ОЙЫНШЫ:', qolUpaiynAlu(oiynshyQoly))
    kartalardyKorsetu(oiynshyQoly)

def qolUpaiynAlu(kartalar):
    upai = 0
    tuzKartaSany = 0

    for karta in kartalar:
        rank = karta[0]
        if rank == 'T':
            tuzKartaSany += 1
        elif rank in ('K', 'D', 'V'):
            upai += 10
        else: 
            upai += int(rank)

    upai += tuzKartaSany
    for i in range(tuzKartaSany):
        if upai + 10 <= 21:
            upai += 10

    return upai

def kartalardyKorsetu(kartalar):
    qatarlar = ['', '', '', '', '']

    for i, karta in enumerate(kartalar):
        qatarlar[0] += ' ___ '
        if karta == KARTA_ARTY:
            qatarlar[1] += '|##_|'
            qatarlar[2] += '|###|'
            qatarlar[3] += '|_##|'
        else: 
            rank, mast = karta
            qatarlar[1] += f'|{rank.ljust(2)} |'
            qatarlar[2] += f'| {mast} |'
            qatarlar[3] += f'|_{rank.rjust(2, '_')}|'


    for qatar in qatarlar:
        print(qatar)

def juristiAlu(oiynshyQoly, aqsha):
    while True: 
        jurister = ['(H)it', '(S)tand']

        if len(oiynshyQoly) == 2 and aqsha > 0:
            jurister.append('(D)ouble down')

        jurisPrompt = ', '.join(jurister) + '> '
        juris = input(jurisPrompt).upper()
        if juris in ('H', 'S'):
            return juris
        if juris == 'D' and '(D)ouble down' in jurister:
            return juris
        
if __name__ == '__main__':
    main()