user_numbers = input('Введите элементы списка через запятую: ')
numbers = []

if ',' in user_numbers:
    user_numbers = user_numbers.split(',')
elif ';' in user_numbers:
    user_numbers = user_numbers.split(';')
elif '/' in user_numbers:
    user_numbers = user_numbers.split('/')

for key in range(0, len(user_numbers)):
    if user_numbers[key].isdigit():
        numbers.append(int(user_numbers[key]))

numbers = list(set(numbers))
print(numbers)