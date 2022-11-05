import bag_class as bag
import card_class as card

test_bag = bag.Bag()
test_card = card.Card()

def test_bag_init():
    assert len(test_bag.list_bag) == 90
    assert test_bag.list_bag[-1] == 90
    assert test_bag.list_bag[0] == 1

def test_bag_get_number():
    number = test_bag.get_number()
    assert number in test_bag.list_bag

def test_bag_renove_number():
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

