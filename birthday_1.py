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

JUL_AILARY = ['Қаңтар', 'Ақпан', 'Наурыз', 'Сәуір', 'Мамыр', 'Маусым', 'Тамыз', 'Шілде', 'Қыркүйек', 'Қазан', 'Қараша', 'Желтоқсан']

print(f'Міне {jauap} мысал туылған күндер.')
tuylganKunder = tuylganKunderAlu(kezdoisoqTuylganKunderSany)
for i, tuylganKun in enumerate(tuylganKunder):
    if i != 0:
        print(', ', end='')
    jylAilary = JUL_AILARY[tuylganKun.month - 1]
    kundiMatinmenJazu = f'{tuylganKun.day}-ші {jylAilary}'
    print(kundiMatinmenJazu, end='')
