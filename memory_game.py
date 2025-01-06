import random
import time
from utils import screen_cleaner

def generate_sequence(difficulty):
    generated_list = []

    for i in range(difficulty):
        generated_list.append(random.randint(1, 101))

    return generated_list

def get_list_from_user():
    user_list_numbers = input("Please enter a list of numbers using comma to separate (format 1,2,3 ...): ").strip()
    user_list_numbers = user_list_numbers.split(',')

    # Check if each user number is a digit between commas
    if all(number.isdigit() for number in user_list_numbers):
        # convert to list of integers
        final_user_list = [int(number) for number in user_list_numbers]
        return final_user_list
    else:
        return get_list_from_user()


def is_list_equal(generated_list, user_list):
    if generated_list == user_list:
        return True
    else:
        return False

def play_memory(difficulty):
    generated_list = generate_sequence(difficulty)
    print(f"Remember this this numbers: {generated_list}")
    time.sleep(7)
    screen_cleaner()
    user_list = get_list_from_user()

    return is_list_equal(generated_list, user_list)