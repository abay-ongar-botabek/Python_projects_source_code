import random

MAX_SANDAR = 3

def main():
    jasyrynSan = jasyrynSandyAlu()
    print(jasyrynSan)

def jasyrynSandyAlu():
    jalpySandarTizimi = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    random.shuffle(jalpySandarTizimi)
    jasyrynSandar = []
    for i in range(MAX_SANDAR):
        jasyrynSandar.append(jalpySandarTizimi[i])
    return jasyrynSandar


if __name__ == '__main__':
    main()