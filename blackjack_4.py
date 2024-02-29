import random

JUREK = chr(9829)
QIYQ = chr(9830)
QARGA = chr(9824)
SHYBYN = chr(9827)

def main():
    print('This is a Blackjack card game and this is main class')
    aqsha = 5000
    while True:

        print('Сізде бар қаражат: ', aqsha)
        print('Неше қаражат ставка қоясыз?')

        qoiylganStavka = stavkaQabuldau()

        aqsha = aqsha - qoiylganStavka
        if aqsha < 0:
            print('Сіз ұтылдыңыз. Бұл ойын бағдарлама.')
            print('Шын өмірде құмар ойын ойнамаңыз!')
            break

        while True:
            deck = kartaKolodasy()

            dilerQoly = [deck.pop(), deck.pop()]
            oiynshyQoly = [deck.pop(), deck.pop()]
            dilerUpaiy = upaidySanau(dilerQoly)
            oiynshyUpaiy = upaidySanau(oiynshyQoly)

            print('Дилер қолы:', dilerUpaiy)
            kartaSuretinSalu(dilerQoly)

            print('Ойыншы қолы:', oiynshyUpaiy)
            kartaSuretinSalu(oiynshyQoly)

            oiynshyJurisi = oiynshyJurisinQabuldau()

            if oiynshyJurisi == 'A':
                if upaidySanau(oiynshyQoly) > 21:
                    print('Сіз ұтылдыңыз')
                    break
                oiynshyQoly.append(deck.pop)
                oiynshyUpaiy = upaidySanau(oiynshyQoly)

                print('Дилер қолы:')
                kartaSuretinSalu(dilerQoly)

                print('Ойыншы қолы:', oiynshyUpaiy)
                kartaSuretinSalu(oiynshyQoly)


def oiynshyJurisinQabuldau():
    juris = input('(A)lu, (S)top, QUIT-шығу үшін. >').upper()
    return juris


def stavkaQabuldau():
    while True:
        stavka = input('STAVKA > ')
        if not stavka.isdecimal():
            continue
        stavka = int(stavka)
        return stavka

def upaidySanau(kartalar):
    upai = 0
    tuzKartaSany = 0

    for karta in kartalar:
        rank = karta[0]
        if rank == 'T':
            tuzKartaSany += 1
        elif rank in ('В', 'Д', 'К', 'Т'):
            upai += 10
        else: 
            upai += int(rank)

    upai += tuzKartaSany
    for i in range(tuzKartaSany):
        if upai + 10 <= 21:
            upai += 10

    return upai

def kartaSuretinSalu(qoldagyKartalar):
    qatarlar = ['', '', '', '', '']
    for i, karta in enumerate(qoldagyKartalar):
        rank, mast = karta
        qatarlar[0] += ' ___ '
        qatarlar[1] += '|{}|'.format(rank.ljust(3, ' '))
        qatarlar[2] += '| {} |'.format(mast)
        qatarlar[3] += '|{}|'.format(rank.rjust(3, '_'))
    for qatar in qatarlar:
        print(qatar)

def kartaKolodasy():
    koloda = []
    for mast in (JUREK, QIYQ, QARGA, SHYBYN):
        for rank in range(2, 11):
            koloda.append((str(rank), mast))
        for rank in ('В', 'Д', 'К', 'Т'):
            koloda.append((rank, mast))
    random.shuffle(koloda)
    return koloda

if __name__ == '__main__':
    main()