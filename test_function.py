import bag_class as bag
import card_class as card
import player_class as pl
import game_class as g

test_bag = bag.Bag()
test_card = card.Card()
test_player = pl.Player()

def test_bag_init():
    assert len(test_bag.list_bag) == 90
    assert test_bag.list_bag[-1] == 90
    assert test_bag.list_bag[0] == 1

def test_bag_get_number():
    number = test_bag.get_number()
    assert number in test_bag.list_bag

def test_bag_remove_number():
    number = 55
    test_bag.remove_number_bag(number)
    assert number not in test_bag.list_bag
    assert number in test_bag.list_from_bag
    test_bag.list_bag.append(55)
    test_bag.list_from_bag.remove(55)

def test_card_init():
    assert len(test_card.data) == 27
    assert test_card.data.count(0) == 12
    assert isinstance(test_card.data, list)
    for i in range(test_card.column):
        for element in [test_card.data[i], test_card.data[i+9], test_card.data[i+18]]:
            assert element in [k for k in range(i*10+1, (i+1)*10)] or element == 0

def test_card_check_number():
    assert test_card.check_number(55) if 55 in test_card.data else not test_card.check_number(55)
    test_card.set_data_for_test([0, 15, 29, 39, 0, 0, 0, 72, 86, 6, 0, 23, 0, 45, 0, 0, 76, 84, 0, 0, 21, 32, 0, 59, 68, 0, 85])
    assert test_card.check_number(45)
    assert not test_card.check_number(55)

def test_card_remove_number():
    for i in range(11, 20):
        if i in test_card.data:
            test_card.remove_number(i)
            assert test_card.data.count('--') == 1
        break
    for i in range(1, 91):
        test_card.remove_number(i)
    assert test_card.data.count(0) == 12
    assert test_card.data.count('--') == 15

def test_card_check_win():
    test_card.set_data_for_test([0, 18, '--', '--', 0, '--', 0, '--', 0, 0, 0, '--', '--', '--', 0, '--', '--', 0, '--', 0, 0, 37, 0, '--', 0, '--', '--'])
    assert test_card.check_win()
    test_card.set_data_for_test(['--', 0, 0, 37, 44, 51, 0, 78, 0, 0, 0, '--', 0, 0, '--', 69, 75, '--', 0, '--', 0, 0, 47, 0, '--', '--', 81])
    assert not test_card.check_win()

def test_pl_init():
    assert test_player.win == -1
    assert isinstance(test_player.card, card.Card)

def test_pl_comp_move():
    test_player.card.set_data_for_test(['--', 0, 0, 37, 44, 51, 0, 78, 0, 0, 0, '--', 0, 0, '--', 69, 75, '--', 0, '--', 0, 0, 47, 0, '--', '--', 81])
    test_player.comp_move(81)
    assert test_player.card.data == ['--', 0, 0, 37, 44, 51, 0, 78, 0, 0, 0, '--', 0, 0, '--', 69, 75, '--', 0, '--', 0, 0, 47, 0, '--', '--', '--']
    assert 81 not in test_player.card.data
    assert test_player.win == -1
    test_player.comp_move(47)
    assert test_player.win == 1
    test_player.card.set_data_for_test([4, 0, 24, 34, 0, 0, 0, 75, 81, 0, 0, 25, 0, 49, 53, 0, 78, 89, 0, 16, 0, 39, 0, 0, 69, 74, 83])
    test_player.comp_move(3)
    assert test_player.card.data == [4, 0, 24, 34, 0, 0, 0, 75, 81, 0, 0, 25, 0, 49, 53, 0, 78, 89, 0, 16, 0, 39, 0, 0, 69, 74, 83]

def test_pl_player_move():
    test_player = pl.Player()
    test_player.card.set_data_for_test([0, '--', '--', 0, 0, 57, '--', 0, '--', 0, 0, 0, '--', '--', 0, 61, '--', '--', '--', 0, '--', 0, 0, 55, '--', 0, '--'])
    test_player.player_move(12, False)
    assert test_player.win == -1
    assert test_player.card.data == [0, '--', '--', 0, 0, 57, '--', 0, '--', 0, 0, 0, '--', '--', 0, 61, '--', '--', '--', 0, '--', 0, 0, 55, '--', 0, '--']
    test_player.player_move(57, False)
    assert test_player.win == 0
    assert test_player.card.data == [0, '--', '--', 0, 0, 57, '--', 0, '--', 0, 0, 0, '--', '--', 0, 61, '--', '--', '--', 0, '--', 0, 0, 55, '--', 0, '--']
    test_player.player_move(57, True)
    assert 57 not in test_player.card.data
    assert test_player.win == 1
    test_player.player_move(12, True)
    assert test_player.win == 0
    assert test_player.card.data == [0, '--', '--', 0, 0, '--', '--', 0, '--', 0, 0, 0, '--', '--', 0, 61, '--', '--', '--', 0, '--', 0, 0, 55, '--', 0, '--']

def test_game_init():
    game = g.Game(2, 3)
    comp_name_list = []
    for comp in game.comp_list:
        assert isinstance(comp, pl.Player)
        comp_name_list.append(comp.name)
    assert comp_name_list == ['comp #1','comp #2']
    player_name_list = []
    for player in game.player_list:
        assert isinstance(player, pl.Player)
        player_name_list.append(player.name)
    assert player_name_list == ['player #1','player #2','player #3']
    assert len(game.comp_list) == 2
    assert len(game.player_list) == 3
    assert len(game.bag_game.list_bag) == 90
    assert game.bag_game.list_bag == [i for i in range(1, 91)]

def test_game_check_end_game():
    game = g.Game(2, 3)
    game.comp_list[0].win = 1
    game.player_list[2].win = 1
    game.player_list[1].win = 0
    game.check_end_game()
    assert game.end_game

