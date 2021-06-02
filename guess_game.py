import random


def guess_number_game():
    won_message = 'Hurray!!! You guessed right'
    below_message = 'Your guess is too low, guess again'
    above_message = 'Your guess is too high, guess again'

    generate_number = random.randint(1, 10)
    # print(generate_number)

    for i in range(3):
        try:
            user_guess = int(input('Guess a number from 1-10: '))
            if 0 < user_guess < 11:
                if user_guess == generate_number:
                    print(won_message)
                    break
                elif user_guess > generate_number:
                    print(above_message)
                else:
                    print(below_message)
                print()
            else:
                print('Number not in range \n')

            if i == 2:
                print('Oops!!! You did not it correct... The correct number was', generate_number)
        except ValueError:
            print("Invalid response not integer\n")


guess_number_game()

