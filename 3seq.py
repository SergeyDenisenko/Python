list_1 = input('Введите элементы 1-го списка через запятую: ').split(',')
list_2 = input('Введите элементы 2-го списка через запятую: ').split(',')

list_1 = set(list_1)
list_2 = set(list_2)
new_list = list(list_1 - list_2)

print(new_list)
