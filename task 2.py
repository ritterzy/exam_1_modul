def convert_secs(num):
    if num < 3600:
        a = num // 60
        b = num - (a * 60)
        print(f'{a}min ; {b}sec')
    elif num > 3600:
        c = num // 3600
        a = (num-3600) // 60
        b = num - (a*60)-(c*3600)
        print(f'{c}h ; {a}min ; {b}sec')

convert_secs(15)