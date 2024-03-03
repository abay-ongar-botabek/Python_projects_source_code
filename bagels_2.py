import random

MAX_SANDAR = 3

def main():
    jasyrynSan = jasyrynSandyAlu()
    qoldanushyEngizgenSan = ''
    while True:
        qoldanushyEngizgenSan = input('Санды енгізіңіз: >')
        if jasyrynSan == qoldanushyEngizgenSan:
            print('Сіз жасырын санды таптыңыз.')
        else:
            print('Тағы байқап көріңіз')
    

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