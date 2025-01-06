from flask import Flask
from utils import SCORES_FILE_NAME, BAD_RETURN_CODE
import os

app = Flask(__name__)

@app.route("/")
def score_server():
    # need to check if SCORES_FILE_NAME file exists
    if not os.path.exists(SCORES_FILE_NAME):
        return f"<html><head><title>Scores Game</title></head><body><h1>ERROR:</h1><div id='score' style='color:red'>{BAD_RETURN_CODE}</div></body></html>"
    else:
        with open(SCORES_FILE_NAME, "r", encoding="utf-8") as scores_file:
            score = scores_file.read()
        return f"<html><head><title>Scores Game</title></head><body><h1>The score is:</h1><div id='score'>{score}</div></body></html>"