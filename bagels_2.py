import random

MAX_SANDAR = 3
MUMKINDIKTER_SANY = 0

def main():
    MUMKINDIKTER_SANY = 1
    jasyrynSan = jasyrynSandyAlu()
    qoldanushyEngizgenSan = ''
    while True:
        qoldanushyEngizgenSan = input('Санды енгізіңіз: > ')
        if jasyrynSan == qoldanushyEngizgenSan:
            print('Сіз жасырын санды таптыңыз.')
        else:
            print('Тағы байқап көріңіз')
            print(MUMKINDIKTER_SANY)
            MUMKINDIKTER_SANY += 1
            if MUMKINDIKTER_SANY > 10:
                print('Өкінішке орай сіз жасырын санды таппадыңыз.')
                print(f'Жасырын сан: {jasyrynSan} болатын')
                jasyrynSan = jasyrynSandyAlu()
                MUMKINDIKTER_SANY = 1

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