import random

JUREK = chr(9829)
QIYQ = chr(9830)
QARGA = chr(9824)
SHYBYN = chr(9827)

def main():
    aqsha = 5000

    koloda = kartaKolodasy()
    dilerQoly = [koloda.pop(), koloda.pop(), koloda.pop()]
    oiynshyQoly = [koloda.pop(), koloda.pop(), koloda.pop()]
    
    qoldyKorsetu(dilerQoly, oiynshyQoly)

def upaidySanau(qoldagyKarta):
    upai = 0
    for rank, mast in qoldagyKarta:
        if rank in ('2', '3', '4', '5', '6', '7', '8', '9', '10'):
            rank = int(rank)
            upai += rank
        elif rank in ('В', 'Д', 'К'):
            upai += 10

    for rank, mast in qoldagyKarta:
        if rank == 'Т' and upai < 10:
            upai += 11
        elif rank == 'Т' and upai > 10:
            upai += 1
    return upai
    
def qoldyKorsetu(dilerQoly, oiynshyQoly):
    dilerUpaiy = upaidySanau(dilerQoly)
    oiynshyUpaiy = upaidySanau(oiynshyQoly)
    print(f'Дилер қолы: {dilerUpaiy} ұпай')
    kartaSuretinSalu(dilerQoly)
    print(f'Ойыншы қолы: {oiynshyUpaiy} ұпай')
    kartaSuretinSalu(oiynshyQoly)

def kartaSuretinSalu(kartalar):
    qatarlar = ['', '', '', '', '']
    for i, karta in enumerate(kartalar):
        rank, mast = karta
        qatarlar[0] += ' ___ '
        qatarlar[1] += f'|{rank.ljust(3, ' ')}|'
        qatarlar[2] += f'| {mast} |'
        qatarlar[3] += f'|{rank.rjust(3, '_')}|'
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