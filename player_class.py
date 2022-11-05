import card_class as card

class Player:

    def __init__(self):
        self.card = card.Card()
        self.win = -1

    def add_name(self, player_name):
        self.name = player_name

    def player_input(self):
        print(f'Ход игрока {self.name}')
        str_input = ''
        while str_input.lower() not in ['y','n']:
            str_input = input('Надо зачеркнуть выпавшее число: y/n ')
        return True if str_input.lower() == 'y' else False

    def comp_move(self, number):
        if self.card.check_number(number):
            self.card.remove_number(number)
            if self.card.check_win():
                self.win = 1
    def player_move(self, number, play_question):
        if play_question and not self.card.check_number(number):
            self.win = 0
        elif play_question and self.card.check_number(number):
            self.card.remove_number(number)
            if self.card.check_win():
                self.win = 1
        elif not play_question and not self.card.check_number(number):
            pass # идем дальше
        elif not play_question and self.card.check_number(number):
            self.win = 0

