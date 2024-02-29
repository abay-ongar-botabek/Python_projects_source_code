import random

JUREK = chr(9829)
QIYQ = chr(9830)
QARGA = chr(9824)
SHYBYN = chr(9827)

def main():
    aqsha = 5000

    kartalarKolodasy = kartaKolodasy()
    birKarta = kartalarKolodasy.pop()
    print(birKarta)
    kartaSuretinSalu(birKarta)

def kartaSuretinSalu(kartalar):
    qatarlar = ['', '', '', '', '']
    rank = kartalar[0]
    mast = kartalar[1]
    for i in range(len(kartalar)):
        qatarlar[0] = ' ___ '
        qatarlar[1] = f'|{rank.ljust(3, ' ')}|'
        qatarlar[2] = f'| {mast} |'
        qatarlar[3] = f'|{rank.rjust(3, '_')}|'
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