from tic_tac_toe import TicTacToe


def main():
    game = TicTacToe()

    while True:
        game.display_board()
        position = int(input(f"Ход игрока {game.current_player}. Выберите позицию (1-9): "))
        game.make_move(position)

        if game.check_winner():
            game.display_board()
            print(f"Игрок {game.current_player} выиграл!")
            break

        if game.is_board_full():
            game.display_board()
            print("Ничья!")
            break


if __name__ == "__main__":
    main()
