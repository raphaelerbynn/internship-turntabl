import random


def guess(correct_num):
    user_guess = int(input('Guess an integer between 1 and 50: '))
    if 1 < user_guess < 50:
        if user_guess > correct_num:
            print('You going too high')
        elif user_guess < correct_num:
            print('You going too low')
        else:
            print('Congratulations you did it!!!')
            return False
    else:
        print('Enter integer in range')


number_to_guess = random.randint(2, 50)
try:
    cont = True
    attempt = 0
    while cont:
        guess(number_to_guess)
        response = input('You want to continue: ')
        if response in ['N', 'n', 'no', 'No', 'NO']:
            cont = False
        elif response in ['Y', 'y', 'yes', 'Yes', 'YES']:
            cont = True
        else:
            print('Enter valid response next time')
            cont = False
        print()
except ValueError:
    print('Invalid input... exit')





