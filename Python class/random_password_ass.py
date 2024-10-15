import random


def random_password():
    # password length
    length = random.randint(7, 10)
    # Generate random password form ascii Characters between 33 and 126
    password = ''.join(chr(random.randint(33, 126)) for _ in range(length))
    print(f'The password is {password}')
    print(f'{password = }') # f string's flexibility


random_password()
