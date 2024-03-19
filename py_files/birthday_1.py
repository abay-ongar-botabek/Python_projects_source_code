import datetime, random


while True:
    print('Неше туылған күн жасап шығарайын? (Макс: 100)')
    jauap = input('> ')
    if jauap.isdecimal() and (0 < int(jauap) <= 100):
        tkSany = int(jauap)
        break


def tuylganKunderAlu(tkSany):
    tuylganKunder = []
    for i in range(tkSany):
        tkBastalatynUaqyt = datetime.date(2001, 1, 1)
        kezdoisoqKun = datetime.timedelta(random.randint(0, 364))
        tuylganKun = tkBastalatynUaqyt + kezdoisoqKun
        tuylganKunder.append(tuylganKun)
    return tuylganKunder

kezdoisoqTuylganKunderSany = int(jauap)
# tyuylganKunder = tuylganKunderAlu(kezdoisoqTuylganKunderSany)
# for i in range(len(tyuylganKunder)):
#     print(tyuylganKunder[i])

JUL_AILARY = ['Қаңтар', 'Ақпан', 'Наурыз', 'Сәуір', 'Мамыр', 'Маусым', 'Шілде', 'Тамыз', 'Қыркүйек', 'Қазан', 'Қараша', 'Желтоқсан']

print(f'Міне {jauap} туылған күн мысалы.')
tuylganKunder = tuylganKunderAlu(kezdoisoqTuylganKunderSany)
for i, tuylganKun in enumerate(tuylganKunder):
    if i != 0:
        print(', ', end='')
    jylAilary = JUL_AILARY[tuylganKun.month - 1]
    kundiMatinmenJazu = f'{tuylganKun.day} {jylAilary}'
    print(kundiMatinmenJazu, end='')


def saikesTk(tuylganKunder):
    if len(tuylganKunder) == len(set(tuylganKunder)):
        return None
    
    for a, tuylganKunA in enumerate(tuylganKunder):
        for b, tuylganKunB in enumerate(tuylganKunder[a+1:]):
            if tuylganKunA == tuylganKunB:
                return tuylganKunA
            
saikesTuylganKunder = saikesTk(tuylganKunder)
print()

print('')
if saikesTuylganKunder != None:
    jylAilary = JUL_AILARY[tuylganKun.month - 1]
    kundiMatinmenJazu = f'{tuylganKun.day} {jylAilary}'
    print(f'{kundiMatinmenJazu} күні туылған бірнеше адам бар')
else:
    print('Бір күнде туылған адамдар табылмады')

simSaikestigi = 0

for i in range(100_000):
    if i % 10_000 == 0:
        i += 10000
        print(f'{i} симуляция жүрді ...')
    tuylganKunder = tuylganKunderAlu(tkSany)
    if saikesTk(tuylganKunder) != None:
        simSaikestigi += 1
print('100 000 симуляция жүрді.')

yqtyimaldyq = round(simSaikestigi/100_000 * 100, 2)
print(f'{tkSany} адам үшін бірдей туылған күн ықтималдылығы: {yqtyimaldyq}')



