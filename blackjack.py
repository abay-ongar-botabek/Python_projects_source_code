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
        tigis = tigistiQabyldau(aqsha)

        koloda = kalodaAlu()
        dilerQoly = [koloda.pop(), koloda.pop()]
        oiynshyQoly = [koloda.pop(), koloda.pop()]

        print('Сіз тіккен ақша:', tigis)
        while True:
            qoldyKorsetu(oiynshyQoly, dilerQoly, False)
            print()

            if qolUpaiynAlu(oiynshyQoly) > 21:
                break

            juris = juristiAlu(oiynshyQoly, aqsha - tigis)

            if juris == 'D':
                qosyumshaTigis = tigistiQabyldau(min(tigis, (aqsha - tigis)))
                tigis += qosyumshaTigis
                print(f'Tigis {tigis}-ke ulgaityldy')
                print('Tigis:', tigis)

            if juris in ('H', 'D'):
                janaKarta = koloda.pop()
                rank, mast = janaKarta
                print(f'Siz algan karta {rank} {mast}')
                oiynshyQoly.append(janaKarta)

                if qolUpaiynAlu(oiynshyQoly) > 21:
                    continue

            if juris in ('S', 'D'):
                break

        if qolUpaiynAlu(oiynshyQoly) <= 21:
            while qolUpaiynAlu(dilerQoly) < 17:
                print('Diler karta aldy ...')
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
            print(f'Diler asyp ketti. Siz {tigis}$ utyp aldynyz')
            aqsha += tigis
        elif (oiynshyUpaiy > 21) or (oiynshyUpaiy < dilerUpaiy):
            print('Siz utyldynyz')
            aqsha -= tigis
        elif oiynshyUpaiy > dilerUpaiy:
            print(f'Siz {tigis}$ utyp aldynyz')
            aqsha += tigis
        elif oiynshyUpaiy == dilerUpaiy:
            print("Ten boldy, tigis aqshasy sizge qaitarylady")

        input('Zhalgastyru ushin ENTER pernesin basynyz...')
        print('\n\n')


def tigistiQabyldau(maxTigis):
    while True:
        print(f'Неше ақша тігіске қоясыз? (1-{maxTigis}, немесе QUIT)')
        tigis = input('> ').upper().strip()
        if tigis == 'QUIT':
            print('Ойын үшін рахмет')
            sys.exit()

        if not tigis.isdecimal():
            continue

        tigis = int(tigis)
        if 1 <= tigis <= maxTigis:
            return tigis
        

def kalodaAlu():
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
        print('DILER:', qolUpaiynAlu(dilerQoly))
        kartalardyKorsetu(dilerQoly)
    else:
        print('DILER: ???')
        kartalardyKorsetu([KARTA_ARTY] + dilerQoly[1:])

    print('OIYNSHY:', qolUpaiynAlu(oiynshyQoly))
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