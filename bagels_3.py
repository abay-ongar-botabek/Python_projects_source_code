import random

JASYRYN_SANDAR_CIFRY = 1
BERILETIN_MUMKINDIK_SANY = 10

def main():
    print('PICO PICO. JASYRYN SANDY TABU')
    jasyrynSan = jasyrynSanBeru()

    oiynshyBoljaganSan = ''

    while jasyrynSan != oiynshyBoljaganSan:
        oiynshyBoljaganSan = input('> ')
        if jasyrynSan == oiynshyBoljaganSan:
            print(f'Жасырын сан {jasyrynSan} болатын')
            print('Сіз жасырын санды таптыңыз: ')


def jasyrynSanBeru():
    jasyrynSan = []
    jasyrynSanTirkes = ''
    jalpySandar = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    random.shuffle(jalpySandar)
    for i in range(JASYRYN_SANDAR_CIFRY):
        jasyrynSan.append(jalpySandar[i])
        jasyrynSanTirkes += str(jalpySandar[i])
    return jasyrynSanTirkes

if __name__ == '__main__':
    main()