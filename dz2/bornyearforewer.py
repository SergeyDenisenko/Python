pushkin_year = 1799
pushkin_birthday = 6.06
is_pushkin_year = False
is_pushkin_birthday = False

while not is_pushkin_birthday:
    if not is_pushkin_year:
        writer_year = int(input("The year of A.S. Pushkin's birth? "))
        if pushkin_year == writer_year:
            is_pushkin_year = True
    elif is_pushkin_year and not is_pushkin_birthday:
        writer_birthday = float(input('Enter the birthday of A.S. Pushkin: '))
        if pushkin_birthday == writer_birthday:
            is_pushkin_birthday = True

print('Right')