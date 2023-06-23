# Write your solution here
def who_won(game_board: list):
    player1 = 0
    player2 = 0
    for row in game_board:
        for square in row:
            if square == 1:
                player1 += 1
            elif square == 2:
                player2 += 1
    if player1 > player2:
        return 1
    elif player2 > player1:
        return 2
    return 0
if __name__ == "__main__":
    game_board=[[0,1,0],[0,1,2],[1,2,1]]
    who_won(game_board)
