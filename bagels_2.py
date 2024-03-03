import random

MAX_SANDAR = 3
MUMKINDIKTER_SANY = 10

def main():
    while True:
        jasyrynSan = jasyrynSandyAlu()
        print('Мен 3 цифрлы сан ойладым. Тауып көр')
        oiynshyZhasaganMumkindikSany = 0

        while oiynshyZhasaganMumkindikSany < MUMKINDIKTER_SANY:
            oiynshyBoljaganSan = ''
            while len(oiynshyBoljaganSan) != MAX_SANDAR or not oiynshyBoljaganSan.isdecimal():
                print('Болжам # {}'.format(oiynshyZhasaganMumkindikSany + 1))
                oiynshyBoljaganSan = input('> ')

            komek = tuspaldapKomekBeru(oiynshyBoljaganSan, jasyrynSan)
            print(komek)

            oiynshyZhasaganMumkindikSany += 1

            if oiynshyZhasaganMumkindikSany == MUMKINDIKTER_SANY:
                print('Сіз таба алмадыңыз!')
                print(f'Жасырын сан {jasyrynSan} болатын')
                break

        oiyndyJalgastyramyzba = input('Ойынды жалғасырамыз ба? (иә / жоқ) > ')
        if not oiyndyJalgastyramyzba.lower().startswith('и'):
            break
        

def tuspaldapKomekBeru(qoldanushyEngizgenSan, jasyrynSan):
    if qoldanushyEngizgenSan == jasyrynSan:
        print('Жарайсыз. Сіз жасырын санды таптыңыз!')
    
    komekHabarlama = []
    for i in range(len(qoldanushyEngizgenSan)):
        if qoldanushyEngizgenSan[i] == jasyrynSan[i]:
            komekHabarlama.append('Fermi')
        elif qoldanushyEngizgenSan[i] in jasyrynSan:
            komekHabarlama.append('Pico')
    if len(komekHabarlama) == 0:
        return 'bagels'
    else:
        return ' '.join(komekHabarlama)

def jasyrynSandyAlu():
    jalpySandarTizimi = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    random.shuffle(jalpySandarTizimi)
    jasyrynSandar = []
    jasyrynSandarTirkes = ''
    for i in range(MAX_SANDAR):
        jasyrynSandar.append(jalpySandarTizimi[i])
        jasyrynSandarTirkes += jalpySandarTizimi[i]
    return jasyrynSandarTirkes


if __name__ == '__main__':
    main()