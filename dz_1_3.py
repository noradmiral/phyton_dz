for n in range(1, 101):
    if n != 11 and n % 10 == 1:
        print(f'{n} процент')
    elif (12 != n and n % 10 == 2) or (13 != n and n % 10 == 3) or (14 != n and n % 10 == 4):
        print(f'{n} процента')
    else:
        print(f'{n} процентов')