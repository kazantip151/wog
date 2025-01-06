from guess_game import play_guess
from memory_game import play_memory
from currency_roulette_game import play_currency
from score import add_score

def welcome():
    player_name = input("Enter your name: ")
    print(f'Hi {player_name} and welcome to the World of Games: The Epic Journey')


def start_play():
    print('''Choose a game to play:
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
    2. Guess Game - guess a number and see if you chose like the computer
    3. Currency Roullete - try and guess the value of a random amount of USD in ILS''')

    game = input("Please select a game (1/2/3): ").strip()

    try:
        game = int(game)
    except ValueError:
        print("Please select a valid game number (must be integer)")
        return start_play()

    if game not in [1, 2, 3]:
        print("Please select a valid game")
        return start_play()

    difficulty = input("Please select difficulty (from 1 to 5): ").strip()

    try:
        difficulty = int(difficulty)
    except ValueError:
        print("Please select a valid difficulty number (must be integer)")
        return start_play()

    if difficulty not in [1, 2, 3, 4, 5]:
        print("Please select a valid difficulty")
        return start_play()

    if game == 1:
        result = play_memory(difficulty)
        if result:
            add_score(difficulty)
            print("You won!")
            return start_play()
        else:
            print("You lost!")
            return start_play()
    elif game == 2:
        result = play_guess(difficulty)
        if result:
            add_score(difficulty)
            print("You won!")
            return start_play()
        else:
            print("You lost!")
            return start_play()
    elif game == 3:
        result = play_currency(difficulty)
        if result:
            add_score(difficulty)
            print("You won!")
            return start_play()
        else:
            print("You lost!")
            return start_play()