# -------------------------------- #
#   Riddle Game v4 (Flask)
#   Web Endpoints
#   By: Jon Zlotnik
# -------------------------------- #

from flask import Flask, request
from flask_cors import CORS
import json
from riddle_game_v3 import *

app = Flask("hello_world")
CORS(app)


@app.route('/getRiddle')
def get_riddle_endpoint():
    return get_riddle()


@app.route('/checkAnswer', methods=['POST'])
def check_answer_endpoint():
    answer = request.get_data().decode('utf8')
    append_user_answer_to_file(user_answers_filename, answer)
    if check_answer(answer, get_correct_answer()):
        return "correct"
    return "incorrect"


@app.route('/getPastAnswers')
def get_past_answers_endpoint():
    return json.dumps(get_past_answers_from_file(user_answers_filename))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')
