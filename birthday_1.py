


while True:
    print('Неше туылған күн жасап шығарайын? (Макс: 100)')
    jauap = input('> ')
    if jauap.isdecimal() and (0 < int(jauap) <= 100):
        tkSany = int(jauap)
        break
print(jauap)
