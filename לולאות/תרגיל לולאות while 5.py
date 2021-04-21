while True:
    DD = input('Insert day: ')

    while not 1 <= int(DD) <= 31:
        print('Invalid day')
        DD = input('Insert day: ')
    DD = int(DD)

    MM = input('Insert month: ')
    while not 1 <= int(MM) <= 12:
        print('Invalid month')
        MM = input('Insert month: ')
    MM = int(MM)

    YY = input('Insert year: ')
    while not 1950 <= int(YY) <= 2025:
        print('Invalid year')
        YY = input('Insert year: ')
    YY = int(YY)

    print(f'{DD}/{MM}/{YY // 10 % 10}{YY % 10}')