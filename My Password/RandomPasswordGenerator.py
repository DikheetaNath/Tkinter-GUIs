# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


class Randompassword:

    def __init__(self):
        self.password = self.generate_password()

    def generate_password(self):

        password_letters = [random.choice(letters) for i in range(random.randint(4, 6))]
        password_numbers = [random.choice(numbers) for i in range(random.randint(2, 4))]
        password_symbols = [random.choice(symbols) for i in range(random.randint(2, 4))]

        password_list = password_letters + password_numbers + password_symbols
        random.shuffle(password_list)

        password = "".join([item for item in password_list])

        return password
