import random
import requests

def get_money_interval():
    dollar = random.randint(1, 100)
    exchange_rates = requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()

    dollar_rate = exchange_rates['rates']['ILS']
    shekel = round(dollar * dollar_rate, 2)
    return {"dollar": dollar, "shekel": shekel}


def get_guess_from_user(dollar):
    user_guess = input(f"Please guess a converted value in ILS for {dollar} USD: ").strip()

    try:
        user_guess = round(float(user_guess), 2)
        return user_guess
    except ValueError:
        print(f"A valid number must be integer. Please try again.")
        return get_guess_from_user(dollar)

def compare_results(shekel, user_guess_number, difficulty):
    allowed_difference = 10 - int(difficulty)
    high_level = shekel + allowed_difference
    low_level = shekel - allowed_difference

    if low_level <= user_guess_number <= high_level:
        return True
    else:
        return False

def play_currency(difficulty):
    currency = get_money_interval()
    user_guess_number = get_guess_from_user(currency['dollar'])
    return compare_results(currency['shekel'], user_guess_number, difficulty)