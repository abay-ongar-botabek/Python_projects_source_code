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
            print('Сіздің қаражатыңыз бітті.')
            print('Бұл тек ойын. Шын өмірде құмар ойындар ойнамаңыз!')
            sys.exit()
        print(f'Сізде бар қаражат: {aqsha}')
        stavka = stavkanyQabyldau(aqsha)
        
        koloda = kartaKolodasy()
        dilerQoly = (koloda.pop(), koloda.pop())
        oiynshyQoly = (koloda.pop(), koloda.pop())
        print(dilerQoly, oiynshyQoly)

def stavkanyQabyldau(maximaldyStavka):
    while True:
        print(f'Неше ақша тігіске қоясыз? 1 - {maximaldyStavka}')
        stavka = input('> ').upper().strip()

        if stavka == 'QUIT':
            print("Ойын үшін рахмет!")
            sys.exit()

        if not stavka.isdecimal():
            continue

        stavka = int(stavka)
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

if __name__ == '__main__':
    main()