# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str):

    if x<=2 and y<=2 and piece=="X" or piece=="O":
        game_board[y][x]=piece
        return True
    else:
        return False

if __name__ == "__main__":
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    play_turn(game_board, 0, 0, "X")
    play_turn(game_board, 2, 0, "X")
    print(game_board)
    