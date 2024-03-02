import random

SAN_CIFRY = 3
MAX_BOLJAM = 10

def main():
    while True:
        qupiaSan = qupiaSandyAlu()
        print('Мен бір құпия санды ойладым.')
        print('Құпия санды табу үшін сізде {} мүмкіндік қалды'.format(MAX_BOLJAM))

        jasalganBoljamSany = 1
        while jasalganBoljamSany <= MAX_BOLJAM:
            boljam = ''
            while len(boljam) != SAN_CIFRY or not boljam.isdecimal():
                print('Болжам# {}'.format(jasalganBoljamSany))
                boljam = input('> ')
            
            tuspalKomek = komekAlu(boljam, qupiaSan)
            print(tuspalKomek)
            jasalganBoljamSany += 1

            if boljam == qupiaSan:
                break

            if jasalganBoljamSany > MAX_BOLJAM:
                print('Сіз мүмкін болжам санынан асып кеттіңіз!')
                print('Жауап {} саны болатын'.format(qupiaSan))

        print('Тағы ойнағыңыз келеді ме? (иә не жоқ)')
        if not input('> ').lower().startswith('и'):
            print('Ойын үшін рахмет.')
            break


def komekAlu(boljam, qupiaSan):
    if boljam == qupiaSan:
        return 'Сіз құпия санды таптыңыз!'
    
    komek = []

    for i in range(len(boljam)):
        if boljam[i] == qupiaSan[i]:
            komek.append('Fermi')
        elif boljam[i] in qupiaSan:
            komek.append('Pico')
    if len(komek) == 0:
        return 'Bagels'
    else:
        komek.sort()
        return ' '.join(komek)

def qupiaSandyAlu():
    jasyrynSan = []
    sandar = [i for i in range(10)]
    random.shuffle(sandar)
    for i in range(SAN_CIFRY):
        jasyrynSan.append(sandar[i])
    tirkesJasyrynSan = ''
    for i in range(len(jasyrynSan)):
        tirkesJasyrynSan += str(jasyrynSan[i])
    return tirkesJasyrynSan

if __name__ == '__main__':
    main()