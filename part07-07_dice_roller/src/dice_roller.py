# Write your solution here
import random

def roll(die: str):
    A = [3, 3, 3, 3, 3, 6]
    B = [2, 2, 2, 5, 5, 5]
    C = [1, 4, 4, 4, 4, 4]

    if die == "A":
        return random.choice(A)
    if die == "B":
        return random.choice(B)
    if die == "C":
        return random.choice(C)

def play(die1: str, die2: str, times: int):
    die1_wins = 0
    die2_wins = 0
    ties = 0

    for i in range(times):
        result1 = roll(die1)
        result2 = roll(die2)

        if result1 > result2:
            die1_wins += 1
        elif result2 > result1:
            die2_wins += 1
        else:
            ties += 1

    return die1_wins, die2_wins, ties

if __name__ == "__main__":
    result = play("A", "B", 100)
    print(result)

    

