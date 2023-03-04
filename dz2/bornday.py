pushkin_year = 1799
pushkin_birthday = 6.06
writer_year = int(input("The year of A.S. Pushkin's birth? "))

if pushkin_year == writer_year:
    writer_birthday = float(input('Enter the birthday of A.S. Pushkin: '))
    if pushkin_birthday == writer_birthday:
        print('Right')
    else:
        print('Wrong birthday')
else:
    print('Wrong year')