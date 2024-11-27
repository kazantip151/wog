def welcome():
    player_name = input("Enter your name: ")
    print(f'Hi {player_name} and welcome to the World of Games: The Epic Journey')


def start_play():
    print("Choose a game to play:")
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    print("2. Guess Game - guess a number and see if you chose like the computer")
    print("3. Currency Roullete - try and guess the value of a random amount of USD in ILS")

    game = input("Please select a game (1/2/3): ")

    difficulty = input("Please select difficulty (from 1 to 5): ")

