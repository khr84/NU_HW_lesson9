import card_class as card

class Player:

    def __init__(self, player_name):
        self.card = card.Card()
        self.name = player_name
        self.win = -1

    def __str__(self):
        return f'{self.name}, card: {self.card}'

    def __eq__(self, other):
        if isinstance(other, card.Card):
            return self.card == other
        elif isinstance(other, Player):
            return self.card == other.card
        elif isinstance(other, list):
            return self.card == other
        else:
            return False

    def player_input(self):
        print(f'Ход игрока {self.name}')
        str_input = ''
        while str_input.lower() not in ['y','n']:
            str_input = input('Надо зачеркнуть выпавшее число: y/n ')
        return True if str_input.lower() == 'y' else False

    def comp_move(self, number):
        if number in self.card:
            self.card.remove_number(number)
            if self.card.check_win():
                self.win = 1

    def player_move(self, number, play_question):
        if play_question and number not in self.card:
            self.win = 0
        elif play_question and number in self.card:
            self.card.remove_number(number)
            if self.card.check_win():
                self.win = 1
        elif not play_question and number not in self.card:
            pass # идем дальше
        elif not play_question and number in self.card:
            self.win = 0
