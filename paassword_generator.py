import random
import string


def generate_random_password(length):
    if length > 0:
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        num = string.digits
        character = string.punctuation

        putting_together = lowercase + uppercase + num + character
        # print(len(putting_together))


        sampling = random.sample(putting_together, length)
        # print(sampling)

        password = ''.join(sampling)
        print('Generated password:', password)
    else:
        print('Password length cannot be negative or 0')


try:
    user_input_length = int(input('Input length of password: '))
    generate_random_password(user_input_length)
except ValueError:
    print('Password length must be an integer not above 94')



