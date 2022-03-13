import string
from random import *

class password_generator():
    characters = string.ascii_letters + string.punctuation  + string.digits

    def __init__(self) -> None:
        self.generate_pass()

    def generate_pass(self, length=randint(8, 16)):
        password =  ''.join(choice(self.characters) for x in range(length))
        print(password)