import random

# Ахматова Анна Андреевна '23.06.1889',
# Блок Александр Александрович '28.11.1880',
# Булгаков Михаил Афанасьевич '15.05.1891',
# Бунин Иван Алексеевич '22.10.1870',
# Грибоедов Александр Сергеевич '15.01.1795',
# Есенин Сергей Александрович '03.10.1895',
# Крылов Иван Андреевич '13.02.1769',
# Лермонтов Михаил Юрьевич '15.10.1814',
# Маяковский Владимир Владимирович '19.07.1893',
# Некрасов Николай Алексеевич '10.12.1821'

birthdays = {
    'akhmatova': '23.06.1889',
    'block': '28.11.1880',
    'bulgakov': '15.05.1891',
    'bunin': '22.10.1870',
    'griboedov': '15.01.1795',
    'esenin': '03.10.1895',
    'krylov': '13.02.1769',
    'lermontov': '15.10.1814',
    'mayakovsky': '19.07.1893',
    'nekrasov': '10.12.1821'
}

full_names = {
    'akhmatova': 'Ахматова Анна Андреевна',
    'block': 'Блок Александр Александрович',
    'bulgakov': 'Булгаков Михаил Афанасьевич',
    'bunin': 'Бунин Иван Алексеевича',
    'griboedov': 'Грибоедов Александр Сергеевич',
    'esenin': 'Есенин Сергей Александрович',
    'krylov': 'Крылов Иван Андреевич',
    'lermontov': 'Лермонтов Михаил Юрьевич',
    'mayakovsky': 'Маяковский Владимир Владимирович',
    'nekrasov': 'Некрасов Николай Алексеевич'
}

months = ('января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря')

def ordinal_date(number):
    number = int(number)
    category_1 = ('перв', 'втор', 'тре', 'четверт', 'пят', 'шест', 'седьм', 'восьм', 'девят', 'десят')
    category_2 = ('один', 'два', 'три', 'четыр', 'пят', 'шест', 'сем', 'восем', 'девят', 'десят')
    end = 'ое'
    exception_end = 'тье'
    ending = 'надцат'

    if number in (1, 2) or number in tuple(range(4, 11)):
        number -= 1
        text = category_1[number] + end
    elif number == 3:
        number -= 1
        text = category_1[number] + exception_end
    elif number == 11 or number in tuple(range(13, 20)):
        number -= 11
        text = category_2[number] + ending + end
    elif number == 12:
        number -= 11
        text = category_2[number][:2] + 'е' + ending + end
    elif number in (20, 30):
        number = number // 10 - 1
        text = category_2[number[:1]] + ending[2:] + end
    elif number == 23:
        number1 = number // 10 - 1
        number2 = number % 10 - 1
        text = category_2[number1] + ending[2:] + 'ь ' + category_1[number2] + exception_end
    elif number > 20:
        number1 = number // 10 - 1
        number2 = number % 10 - 1
        text = category_2[number1] + ending[2:] + 'ь ' + category_1[number2] + end
    return text

quantity = 5
correct = 0
victory = True
birthdays_keys = random.sample(list(birthdays.keys()), quantity)

while victory:
    for key in birthdays_keys:
        answer = input(f'Введите день рождение "{full_names[key]}": ')
        if answer == birthdays[key]:
            correct += 1
        else:
            date_list = birthdays[key].split('.')
            print('Correct answer: ', ordinal_date(date_list[0]), months[int(date_list[1]) - 1], date_list[2], 'года')

    print('Correct answers:', correct)
    print('Mistakes', quantity - correct)
    print('Percentage of correct answers:', correct * 100 / quantity)
    print('Percentage of incorrect answers:', (quantity - correct) * 100 / quantity)

    while True:
        end = input('Start the game first? (yes/no) ')
        if end in ('yes', 'y'):
            correct = 0
            birthdays_keys = random.sample(list(birthdays.keys()), quantity)
            break
        elif end in ('no', 'n'):
            victory = False
            break