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
            print('Сізде ақша бітті.')
            print('Бұл ойын. Шын өмірде құмар ойын ойнамаңыз!')
            sys.exit()

        print(f'Сізде бар қаражат: {aqsha}')
        stavka = stavkaQabyldau(aqsha)

        karta_kolodasy = kartaKolodasynAralastyru()

        dilerQoly = [karta_kolodasy.pop(), karta_kolodasy.pop()]
        oiynshyQoly = [karta_kolodasy.pop(), karta_kolodasy.pop()]

        print(f'Сіз тіккен ақша: {stavka}')
        while True:
            qoldyKorsetu(dilerQoly, oiynshyQoly, False)

            if upaidySanau(oiynshyQoly) > 21:
                break

            juris = juristiQabyldau(oiynshyQoly, aqsha-stavka)

            if juris == 'A':
                oiynshyQoly.append(karta_kolodasy.pop())

                if upaidySanau(oiynshyQoly) > 21:
                    continue

            if juris == 'S':
                break

        if upaidySanau(oiynshyQoly) <= 21:
            while upaidySanau(dilerQoly) < 17:
                print('Дилер карта алды ...')
                dilerQoly.append(karta_kolodasy.pop())
                qoldyKorsetu(dilerQoly, oiynshyQoly, False)

                if upaidySanau(dilerQoly) > 21:
                    break
                input('Жалғастыру үшін ENTER пернесін басыңыз...')

        oiynshyUpaiy = upaidySanau(oiynshyQoly)
        dilerUpaiy = upaidySanau(dilerQoly)

        if dilerUpaiy > 21:
            aqsha += stavka
            print('******************************')
            print('Дилер асып кетті. Сіз ұттыңыз')
        elif oiynshyUpaiy > 21 or dilerUpaiy > oiynshyUpaiy:
            aqsha -= stavka
            print('******************************')
            print('Сіз ұтылдыңыз.')
        elif oiynshyUpaiy == dilerUpaiy:
            print('******************************')
            print('Тең болды. Ставка қайтарылады')
        elif oiynshyUpaiy > dilerUpaiy:
            print('******************************')
            print('Сіз ұттыңыз.')
            aqsha += stavka

        print('Ойынды жалғастыру үшін ENTER пернесін басыңыз.')

        qoldyKorsetu(dilerQoly, oiynshyQoly, True)
        



            
            
              

def stavkaQabyldau(maximaldyStavka):
    while True:
        print(f'Неше теңге ставка қоясыз? 1-{maximaldyStavka}')
        stavka = input('> ').upper().strip()
        if not stavka.isdecimal():
            continue
        stavka = int(stavka)
        maximaldyStavka -= stavka
        return stavka

def kartaKolodasynAralastyru():
    karta_kolodasy = []
    for mast in (JUREK, QIYQ, QARGA, SHYBYN):
        for rank in range(2, 11):
            karta_kolodasy.append((str(rank), mast))
        for rank in ('В', 'Д', 'К', 'Т'):
            karta_kolodasy.append((rank, mast))
    random.shuffle(karta_kolodasy)
    return karta_kolodasy

def kartaSuretinSalu(kartalar):
    qatarlar = ['', '', '', '', '', '']
    for i, karta in enumerate(kartalar):
        qatarlar[0] += ' ___ '
        if karta == KARTA_ARTY:
            qatarlar[1] += '|#__|'
            qatarlar[2] += '|_##|'
            qatarlar[3] += '|__#|'
        else:
            rank, mast = karta
            qatarlar[1] += f'|{rank.ljust(3, ' ')}|'
            qatarlar[2] += f'| {mast} |'
            qatarlar[3] += f'|{rank.rjust(3, '_')}|'

    for qatar in qatarlar:
        print(qatar)

def upaidySanau(kartalar):
    upai = 0
    qoldagyTuzdarSany = 0

    for karta in kartalar:
        rank = karta[0]
        if rank == 'Т':
            qoldagyTuzdarSany += 1
        elif rank in ('В', 'Д', 'К'):
            upai += 10
        else:
            upai += int(rank)
    
    upai += qoldagyTuzdarSany
    for i in range(qoldagyTuzdarSany):
        if (upai + 10) <= 21:
            upai += 10
        
    return upai

def qoldyKorsetu(dilerQoly, oiynshyQoly, dilerQolynKorsetu):
    if dilerQolynKorsetu:
        dilerUpaiy = upaidySanau(dilerQoly)
        print(f'Дилердің ұпайы: {dilerUpaiy}')
        kartaSuretinSalu(dilerQoly)
    else:
        print('Дилер ұпайы: ???')
        kartaSuretinSalu([KARTA_ARTY] + dilerQoly[1:])
    
    oiynshyUpaiy = upaidySanau(oiynshyQoly)
    print(f'Ойыншы ұпайы: {oiynshyUpaiy}')
    kartaSuretinSalu(oiynshyQoly)

def juristiQabyldau(oiynshyQoly, aqsha):
    while True:
        jurister = ['(A)lu', '(S)top']

        if (len(oiynshyQoly) == 2 and aqsha > 0):
            jurister.append('(D)ouble down')

        jurisPrompt = ', '.join(jurister) + ' > '
        juris = input(jurisPrompt).upper()
        if juris in ('A', 'S'):
            return juris
        if juris == 'D' and '(D)double down' in jurister:
            return juris

if __name__ == '__main__':
    main()