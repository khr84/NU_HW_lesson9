import random
import numpy as np

class Card:

    row = 3
    column = 9
    num_empty = 4

    def __init__(self):
        self.data = []
        # формируем таблицу 3х9 с учетом того что в каждом будущем столбце числа из одного десятка
        matrix_number = [random.sample([number for number in range(1, 10)], self.row)]
        for i in range(1, self.column):
            matrix_number = np.vstack([matrix_number, random.sample([number for number in range(1 + i * 10, 10 + i * 10)], self.row)])

        # разворачиваем таблицу 9х3
        matrix_number = np.transpose(matrix_number)

        # убираем до 4 элементов в каждой строке, и не более 2 в каждом столбце
        while np.count_nonzero(matrix_number) > (self.column - self.num_empty) * self.row:
            i = random.randint(0, self.row - 1)
            j = random.randint(0, self.column - 1)
            if matrix_number[i][j] != 0:
                # проверка в i-й строке 3 и меньше 0, в j-м столбце 1 или нет нулей
                if list(matrix_number[i, :]).count(0) < 4 and list(matrix_number[:, j]).count(0) < 2:
                    matrix_number[i][j] = 0

        # складываем построчно в список
        for i in range(self.row):
                self.data.extend(list(matrix_number[i,  : ]))

    def set_data_for_test(self, list_number):
        self.data = list_number

    def print_card(self, player_name = ''):
        count_symb = ((self.column * 3 - 1) - len(player_name) - 2) // 2
        print(f'{"*" * count_symb} {player_name} {"*" * ((self.column * 3 - 1) - count_symb - len(player_name) - 2)}')
        print_str = ''
        for i in range(len(self.data)):
            # если первый элемент строки, то начинаем заново формировать строку
            if (i+1) % self.column == 1:
                print_str = ''
            # 0 заменяем на пусто
            if self.data[i] == 0:
                element = '  '
            # увеличиваем до 2-х знаков каждый символ
            elif len(str(self.data[i])) == 1:
                element = f' {self.data[i]}'
            else:
                element = str(self.data[i])
            # собираем строку
            print_str += f'{element} '
            # после обработки каждого 9-го элемента печатаем строку
            if (i+1) % self.column == 0:
                print(f'{print_str}')
        print('*' * (self.column * 3 - 1))

    def check_number(self, number):
        return True if number in self.data else False

    def remove_number(self, number):
        for i in range(len(self.data)):
            if self.data[i] == number:
                self.data[i] = '--'

    def check_win(self):
        win = []
        for i in range(self.row):
            # проверка что в однй из строк зачеркнуты все 5 цифр
            win.append(1) if self.data[self.column * i : self.column * (i+1)].count('--') == 5 else win.append(0)
        return True if win.count(1) > 0 else False
