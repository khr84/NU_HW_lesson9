import player_class as pl
import bag_class as bag

class Game:

    end_game = False

    def __init__(self, count_comp, count_player):
        self.bag_game = bag.Bag()

        self.win_player = []
        self.win_comp = []
        self.lose_player = []

        self.comp_list = []
        for i in range(count_comp):
            comp =  pl.Player(f'comp #{i+1}')
            self.comp_list.append(comp)

        self.player_list = []
        for i in range(count_player):
            gamer = pl.Player(f'player #{i + 1}')
            self.player_list.append(gamer)

    def __str__(self):
        players = []
        for player in self.comp_list:
            players.append(str(player))
        for player in self.player_list:
            players.append(str(player))
        return str(players)

    def __eq__(self, other):
        return True if len(self.comp_list) == len(other.comp_list) and len(self.player_list) == len(other.player_list) else False

    def do_move(self):
        number = self.bag_game.get_number()
        print(f'\nВыпало число: {number}')
        self.bag_game.remove_number_bag(number)
        # ход компа/игрока
        for comp in self.comp_list:
            comp.card.print_card(comp.name)
            comp.comp_move(number)
        for player in self.player_list:
            print()
            player.card.print_card(player.name)
            play_question = player.player_input()
            player.player_move(number, play_question)

    def check_end_game(self):
        self.win_comp = [comp.name for comp in self.comp_list if comp.win == 1]
        self.win_player = [player.name for player in self.player_list if player.win == 1]
        self.lose_player = [player.name for player in self.player_list if player.win == 0]
        if len(self.win_comp) > 0 or len(self.win_player) > 0 or len(self.lose_player) > 0:
            self.end_game = True

    def print_game(self):
        print('Конец игры!')
        win_list = []
        if len(self.win_comp) > 0 or len(self.win_player) > 0:
            win_list.extend(self.win_comp)
            win_list.extend(self.win_player)
            print(f'В игре попедил(и): {win_list}')
        if len(self.lose_player) > 0:
            print(f'В игре проиграл(и): {self.lose_player}')
        print(f'Невыпавшие номера: {self.bag_game.list_bag}')