def seizoen(maand):
    if maand == 12:
        print('Winter')
    elif maand > 8:
        print('Herfst')
    elif maand > 5:
        print('Zomer')
    elif maand > 2:
        print('Lente')
    else:
        print('Winter')

seizoen(8)