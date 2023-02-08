from enum import Enum
from flask import Flask, render_template, request

application = Flask(__name__, template_folder="templates")


class PlayerEnum(str, Enum):
    FIRST = "F"
    SECOND = "S"


def move_handler(board, player):
    # first dont give to opponent win
    column = board_scanner_for_move(board, player)

    if column:
        return {"column": column}
    # second watch to our win condition
    column = board_scanner_for_move(board, player, opponent=False)
    return {"column": column}


def board_scanner_for_move(board, player, opponent=True):
    # scans board
    ...



@application.route("/healthz")
def index():
    return render_template('heathz.html')


@application.route("/move", methods=["POST", "GET"])
def move():
    if request.method == 'POST':
        data = request.data
        board, player = data['board'], data['player']
        return move_handler(board, player)
    return {"message": "Cringe"}


if __name__ == "__main__":
    application.run(host='0.0.0.0', port='8080', debug=True)
