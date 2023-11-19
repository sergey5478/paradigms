class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"

    def display_board(self):
        """Цикл с шагом в 3. Делаем срез от i до i+3 и
        соединяем через |. Печатаем результат."""
        for i in range(0, 9, 3):
            print("|".join(self.board[i:i + 3]))

    def make_move(self, position):
        """Проверка позиции и по индексу(свободна ли?). Если да
        записываем X(первого игрока) и вызываем следующий метод."""
        if 1 <= position <= 9 and self.board[position - 1] == " ":
            self.board[position - 1] = self.current_player
            self.switch_player()
        else:
            print("Недопустимый ход. Повторите.")

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        """Проверка строк, столбцов и диагоналей на наличие выигрышных комбинаций"""
        for i in range(0, 3):
            # Проверка строк
            if self.board[i] == self.board[i + 3] == self.board[i + 6] != " ":
                return True
            # Проверка столбцов
            elif self.board[i * 3] == self.board[i * 3 + 1] == self.board[i * 3 + 2] != " ":
                return True
        # Проверка диагоналей
        if self.board[0] == self.board[4] == self.board[8] != " " or \
                self.board[2] == self.board[4] == self.board[6] != " ":
            return True
        return False

    def is_board_full(self):
        return " " not in self.board
