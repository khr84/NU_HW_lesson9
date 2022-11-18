from bag_class import Bag
from card_class import Card
from player_class import Player
from game_class import Game
import unittest

class TestBag(unittest.TestCase):
    def setUp(self):
        self.bag = Bag()
    def test_bag_init(self):
        self.assertEqual(len(self.bag.list_bag), 90)
        self.assertEqual(self.bag.list_bag[-1], 90)
        self.assertEqual(self.bag.list_bag[0], 1)

    def test_bag_get_number(self):
        number = self.bag.get_number()
        self.assertIn(number, self.bag.list_bag)

    def test_bag_remove_number(self):
        number = 55
        self.bag.remove_number_bag(number)
        self.assertNotIn(number, self.bag.list_bag)
        self.assertIn(number, self.bag.list_from_bag)

class TestCard(unittest.TestCase):

    def setUp(self):
        self.card = Card()
    def test_card_init(self):
        self.assertEqual(len(self.card.data), 27)
        self.assertEqual(self.card.data.count(0), 12)
        self.assertIsInstance(self.card.data, list)
        for i in range(self.card.column):
            for element in [self.card.data[i], self.card.data[i+9], self.card.data[i+18]]:
                self.assertTrue(element in [k for k in range(i*10+1, (i+1)*10)] or element == 0)

    def test_card_check_number(self):
        self.assertTrue(self.card.check_number(55) if 55 in self.card.data else not self.card.check_number(55))
        self.card.set_data_for_test([0, 15, 29, 39, 0, 0, 0, 72, 86, 6, 0, 23, 0, 45, 0, 0, 76, 84, 0, 0, 21, 32, 0, 59, 68, 0, 85])
        self.assertTrue(self.card.check_number(45))
        self.assertFalse(self.card.check_number(55))

    def test_card_remove_number(self):
        for i in range(11, 20):
            if i in self.card.data:
                self.card.remove_number(i)
                self.assertEqual(self.card.data.count('--'), 1)
            break
        for i in range(1, 91):
            self.card.remove_number(i)
        self.assertEqual(self.card.data.count(0), 12)
        self.assertEqual(self.card.data.count('--'), 15)

    def test_card_check_win(self):
        self.card.set_data_for_test([0, 18, '--', '--', 0, '--', 0, '--', 0, 0, 0, '--', '--', '--', 0, '--', '--', 0, '--', 0, 0, 37, 0, '--', 0, '--', '--'])
        self.assertTrue(self.card.check_win())
        self.card.set_data_for_test(['--', 0, 0, 37, 44, 51, 0, 78, 0, 0, 0, '--', 0, 0, '--', 69, 75, '--', 0, '--', 0, 0, 47, 0, '--', '--', 81])
        self.assertFalse(self.card.check_win())

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player()
    def test_pl_init(self):
        self.assertEqual(self.player.win, -1)
        self.assertIsInstance(self.player.card, Card)

    def test_pl_comp_move(self):
        self.player.card.set_data_for_test(['--', 0, 0, 37, 44, 51, 0, 78, 0, 0, 0, '--', 0, 0, '--', 69, 75, '--', 0, '--', 0, 0, 47, 0, '--', '--', 81])
        self.player.comp_move(81)
        self.assertEqual(self.player.card.data, ['--', 0, 0, 37, 44, 51, 0, 78, 0, 0, 0, '--', 0, 0, '--', 69, 75, '--', 0, '--', 0, 0, 47, 0, '--', '--', '--'])
        self.assertNotIn(81, self.player.card.data)
        self.assertEqual(self.player.win, -1)
        self.player.comp_move(47)
        self.assertEqual(self.player.win, 1)
        self.player.card.set_data_for_test([4, 0, 24, 34, 0, 0, 0, 75, 81, 0, 0, 25, 0, 49, 53, 0, 78, 89, 0, 16, 0, 39, 0, 0, 69, 74, 83])
        self.player.comp_move(3)
        self.assertEqual(self.player.card.data,  [4, 0, 24, 34, 0, 0, 0, 75, 81, 0, 0, 25, 0, 49, 53, 0, 78, 89, 0, 16, 0, 39, 0, 0, 69, 74, 83])

    def test_pl_player_move(self):
        self.player.card.set_data_for_test([0, '--', '--', 0, 0, 57, '--', 0, '--', 0, 0, 0, '--', '--', 0, 61, '--', '--', '--', 0, '--', 0, 0, 55, '--', 0, '--'])
        self.player.player_move(12, False)
        assert self.player.win == -1
        assert self.player.card.data == [0, '--', '--', 0, 0, 57, '--', 0, '--', 0, 0, 0, '--', '--', 0, 61, '--', '--', '--', 0, '--', 0, 0, 55, '--', 0, '--']
        self.player.player_move(57, False)
        assert self.player.win == 0
        assert self.player.card.data == [0, '--', '--', 0, 0, 57, '--', 0, '--', 0, 0, 0, '--', '--', 0, 61, '--', '--', '--', 0, '--', 0, 0, 55, '--', 0, '--']
        self.player.player_move(57, True)
        assert 57 not in self.player.card.data
        assert self.player.win == 1
        self.player.player_move(12, True)
        assert self.player.win == 0
        assert self.player.card.data == [0, '--', '--', 0, 0, '--', '--', 0, '--', 0, 0, 0, '--', '--', 0, 61, '--', '--', '--', 0, '--', 0, 0, 55, '--', 0, '--']

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game(2, 3)
    def test_game_init(self):
        comp_name_list = []
        for comp in self.game.comp_list:
            self.assertIsInstance(comp, Player)
            comp_name_list.append(comp.name)
        self.assertEqual(comp_name_list,  ['comp #1','comp #2'])
        player_name_list = []
        for player in self.game.player_list:
            self.assertIsInstance(player, Player)
            player_name_list.append(player.name)
        self.assertEqual(player_name_list, ['player #1','player #2','player #3'])
        self.assertEqual(len(self.game.comp_list), 2)
        self.assertEqual(len(self.game.player_list), 3)
        self.assertEqual(len(self.game.bag_game.list_bag), 90)
        self.assertEqual(self.game.bag_game.list_bag, [i for i in range(1, 91)])

    def test_game_check_end_game(self):
        self.game.comp_list[0].win = 1
        self.game.player_list[2].win = 1
        self.game.player_list[1].win = 0
        self.game.check_end_game()
        self.assertTrue(self.game.end_game)

