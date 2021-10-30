list_cubes = []
for i in range(1, 1000, 2):
    list_cubes.append(i ** 3)

result = 0
for i in range(len(list_cubes)):
    sum_cube_numb = 0
    list_cubes_temp = list_cubes[i]
    while list_cubes_temp > 0:
        sum_cube_numb += list_cubes_temp % 10
        list_cubes_temp = list_cubes_temp // 10
    if sum_cube_numb % 7 == 0:
        result += (list_cubes[i])
print(f'Сумма чисел которых делится нацело на 7 составляет: {result}')


result = 0
for i in range(len(list_cubes)):
    list_cubes[i] += 17
    sum_cube_numb = 0
    list_cubes_temp = list_cubes[i]
    while list_cubes_temp > 0:
        sum_cube_numb += list_cubes_temp % 10
        list_cubes_temp = list_cubes_temp // 10
    if sum_cube_numb % 7 == 0:
        result += (list_cubes[i])
print(f'Сумма чисел, увеличенных на 17, сумма цифр которых делится нацело на 7 составляет: {result}')