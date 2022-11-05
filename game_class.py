import player_class as pl
import bag_class as bag

class Game:

    end_game = False

    def __init__(self, count_comp, count_player):
        self.bag_game = bag.Bag()

        self.comp_list = []
        for i in range(count_comp):
            comp =  pl.Player()
            comp.add_name(f'comp #{i+1}')
            self.comp_list.append(comp)

        self.player_list = []
        for i in range(count_player):
            gamer = pl.Player()
            gamer.add_name(f'player #{i + 1}')
            self.player_list.append(gamer)


    def do_move(self):
        number = self.bag_game.get_number()
        print(f'\nВыпало число: {number}')
        self.bag_game.remove_number_bag(number)
        # ход компа/игрока
        for comp in self.comp_list:
            comp.card.print_card(comp.name)
            if comp.card.check_number(number):
                comp.card.remove_number(number)
                if comp.card.check_win():
                    comp.win = 1
        for player in self.player_list:
            print()
            player.card.print_card(player.name)
            play_question = player.player_input()
            player.player_move(number, play_question)

    def check_end_game(self):
        win_comp = [comp.name for comp in self.comp_list if comp.win == 1]
        win_player = [player.name for player in self.player_list if player.win == 1]
        lose_player = [player.name for player in self.player_list if player.win == 0]
        if len(win_comp) > 0 or len(win_player) > 0 or len(lose_player) > 0:
            self.end_game = True
            print('Конец игры!')
        if len(win_comp) > 0 or len(win_player) > 0:
            win_comp.extend(win_player)
            print(f'В игре попедил(и): {win_comp}')
        if len(lose_player) > 0:
            print(f'В игре проиграли: {lose_player}')