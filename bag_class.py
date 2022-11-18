import random

class Bag:

    list_from_bag = []

    def __init__(self):
        self.list_bag = [i for i in range(1,91)]

    def __str__(self):
        return str(self.list_bag)

    def __eq__(self, other):
        if isinstance(other, Bag):
            return self.list_bag == other.list_bag
        elif isinstance(other, list):
            return self.list_bag == other
        else:
            return False
    def get_number(self):
        number = 0
        while number not in self.list_bag:
            number = random.randint(1, 90)
        return number

    def remove_number_bag(self, number):
        self.list_bag.remove(number)
        self.list_from_bag.append(number)