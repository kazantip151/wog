import random

def generate_number(difficulty):
    return random.randint(0, difficulty)


def get_guess_from_user(difficulty):
    user_number = input(f"Please select a number between 0 and {difficulty}: ").strip()
    try:
        user_number = int(user_number)
    except ValueError:
        print(f"A valid number must be integer. Please try again.")
        return get_guess_from_user(difficulty)

    if user_number < 0 or user_number > difficulty:
        return get_guess_from_user(difficulty)
    else:
        return user_number


def compare_results(generated_number, user_number):
    if user_number == generated_number:
        return True
    else:
        return False


def play_guess(difficulty):
    generated_number = generate_number(difficulty)
    user_number = get_guess_from_user(difficulty)
    return compare_results(generated_number, user_number)