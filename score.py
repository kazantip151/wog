from utils import SCORES_FILE_NAME


def add_score(difficulty):
    points_of_winning = (difficulty * 3) + 5

    with open(SCORES_FILE_NAME, "a+", encoding="utf-8") as scores_file:
        scores_file.seek(0)
        previous_result = scores_file.read()

        if len(previous_result) == 0:
            previous_result = 0

        new_score = int(previous_result) + points_of_winning
        scores_file.seek(0)
        scores_file.truncate()
        scores_file.write(str(new_score))