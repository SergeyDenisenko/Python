pushkin_year = 1799
tolstoy_year = 1828
bulgakov_year = 1891
esenin_year = 1895
nekrasov_year = 1821

all_answers = 5
victory = True
victory_end = False

while not victory_end:
    if victory:
        correct_answers = 0
        writer_year = int(input('Year of birth of A.S.Pushkin? '))
        if writer_year == pushkin_year:
            correct_answers += 1
        writer_year = int(input('The year of birth of L.N.Tolstoy? '))
        if writer_year == tolstoy_year:
            correct_answers += 1
        writer_year = int(input('The year of birth of M.A.Bulgakov? '))
        if writer_year == bulgakov_year:
            correct_answers += 1
        writer_year = int(input('Year of birth S.A.Yesenin? '))
        if writer_year == esenin_year:
            correct_answers += 1
        writer_year = int(input('The year of birth of N.A.Nekrasov? '))
        if writer_year == nekrasov_year:
            correct_answers += 1

        print('Correct answers:', correct_answers)
        print('Wrong answers', all_answers - correct_answers)
        print('Percentage of correct answers', correct_answers * 100 // all_answers)
        print('Percentage of wrong answers', (all_answers - correct_answers) * 100 // all_answers)

        victory = False

    victory_start = input('Do you want to start the game over? (enter yes or no) ')
    if victory_start == 'yes':
        victory = True
    elif victory_start == 'no':
        victory_end = True
