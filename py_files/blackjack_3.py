import random, sys

JUREK = chr(9829)
QIYQ = chr(9830)
QARGA = chr(9824)
SHYBYN = chr(9827)

KARTA_ARTY = 'backside'

def main():
    aqsha = 5000 #теңге   

    while True:
        koloda = kartaKolodasy()

        print('Сізде бар қаражат: ', aqsha)
        
        if aqsha <= 0:
            print('Бұл бағдарламалауды үйрететін ойын.')
            print('Шын өмірде құмар ойын ойнамаңыз')
            break

        stavkaKolemi = stavkaQabyldau(aqsha)
        aqsha -= stavkaKolemi
        print(aqsha)

        dilerQoly = (koloda.pop(), koloda.pop())
        oiynshyQoly = (koloda.pop(), koloda.pop())

        qoldyKorsetu(dilerQoly, oiynshyQoly)
        continue

        
def qoldyKorsetu(dilerQoly, oiynshyQoly):
    dilerUpaiy = upaidySanau(dilerQoly)
    oiynshyUpaiy = upaidySanau(oiynshyQoly)

    print('Дилер ұпайы:', dilerUpaiy)
    kartaSuretinSalu(dilerQoly)
    print('Ойыншы ұпайы:', oiynshyUpaiy)
    kartaSuretinSalu(oiynshyQoly)

def stavkaQabyldau(maximaldiStavka):
    while True:
        print('Неше ақша ставка қоясыз?')
        stavka = input('> ').strip()   
        
        if not stavka.isdecimal():
            continue

        stavka = int(stavka)
        if stavka > maximaldiStavka:
            print(f'Сізде бар қаражат {maximaldiStavka}. Одан артық қоя алмайсыз.')
            continue
        return stavka


def upaidySanau(qoldagyKarta):
    upai = 0

    for rank, mast in qoldagyKarta:
        if rank in range(2, 11):
            upai += int(rank)
        elif rank in ('В', 'Д', 'К'):
            upai += 10 

    for rank, mast in qoldagyKarta:
        if upai <= 10 and rank == 'Т':
            upai += 11
        elif upai > 10 and rank == 'Т':
            upai += 1
    
    return upai

def kartaSuretinSalu(kartalar):
    qatarlar = ['', '', '', '', '',]
    
    for i, karta in enumerate(kartalar):
        qatarlar[0] += ' ___ '
        rank, mast = karta
        rank = str(rank)
        qatarlar[1] += f'|{rank.ljust(3, " ")}|'
        qatarlar[2] += f'| {mast} |'
        qatarlar[3] += f'|{rank.rjust(3, "_")}|'
    
    for qatar in qatarlar:
        print(qatar)
        

def kartaKolodasy():
    koloda = []
    for mast in (JUREK, QIYQ, QARGA, SHYBYN):
        for rank in range(2, 11):
            koloda.append((rank, mast))
        for rank in ('В', 'Д', 'К', 'Т'):
            koloda.append((rank, mast))
    random.shuffle(koloda)
    return koloda

if __name__ == '__main__':
    main()