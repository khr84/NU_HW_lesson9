import game_class as g

count_comp = int(input('Введите кол-во игроков компьютеров: '))
count_player = int(input('Введите кол-во игроков: '))
game = g.Game(count_comp, count_player)

while not game.end_game:
    game.do_move()
    game.check_end_game()
    if game.end_game:
        game.print_game()
