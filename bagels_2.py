import random

MAX_SANDAR = 3
MUMKINDIKTER_SANY = 10

def main():
    MUMKINDIKTER_SANY = 1
    jasyrynSan = jasyrynSandyAlu()
    qoldanushyEngizgenSan = ''
    while True:
        qoldanushyEngizgenSan = input('3 цифрдан тұратын санды енгізіңіз: > ')
        if jasyrynSan == qoldanushyEngizgenSan:
            print('Сіз жасырын санды таптыңыз.')
        elif len(qoldanushyEngizgenSan) < 3 or len(qoldanushyEngizgenSan) >= 4:
            continue
        else:
            print('Тағы байқап көріңіз')
            print(MUMKINDIKTER_SANY)
            MUMKINDIKTER_SANY += 1
            if MUMKINDIKTER_SANY > 10:
                print('Өкінішке орай сіз жасырын санды таппадыңыз.')
                print(f'Жасырын сан: {jasyrynSan} болатын')
                jasyrynSan = jasyrynSandyAlu()
                MUMKINDIKTER_SANY = 1

def tuspaldapKomekBeru(qoldanushyEngizgenSan, jasyrynSan):
    if qoldanushyEngizgenSan == jasyrynSan:
        print('Жарайсыз. Сіз жасырын санды таптыңыз!')
    
    komekHabarlama = []
    for i in (len(qoldanushyEngizgenSan)):
        if qoldanushyEngizgenSan[i] == jasyrynSan[i]:
            komekHabarlama.append('Fermi')
        elif qoldanushyEngizgenSan[i] in jasyrynSan:
            komekHabarlama.append('Pico')
        elif qoldanushyEngizgenSan[i] not in jasyrynSan:
            komekHabarlama.append('Bagels')
    ' '.join(komekHabarlama)
    return komekHabarlama

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