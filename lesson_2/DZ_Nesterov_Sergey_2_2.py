lst_1 = ['в', '5', 'часов', '17', 'минут',
         'температура', 'воздуха', 'была', '+5', 'градусов']
lst_2 = []

for item in lst_1:
    if item.isdigit():
        item = f'{int(item):02d}'
        lst_2.append('"')
        lst_2.append(item)
        lst_2.append('"')
    elif item.strip('+').isdigit():
        lst_2.append('"')
        item = item[0] + f'{int(item):02d}'
        lst_2.append(item)
        lst_2.append('"')
    else:
        lst_2.append(item)

print(' '.join(lst_2))