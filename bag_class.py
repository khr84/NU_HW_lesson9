import random

class Bag:

    list_from_bag = []

    def __init__(self):
        self.list_bag = [i for i in range(1,91)]

    def get_number(self):
        number = 0
        while number not in self.list_bag:
            number = random.randint(1, 90)
        return number

    def remove_number_bag(self, number):
        self.list_bag.remove(number)
        self.list_from_bag.append(number)