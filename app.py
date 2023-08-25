from flask import Flask, request, render_template, jsonify
from uuid import uuid4

from boggle import BoggleGame

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-secret"

# The boggle games created, keyed by game id
games = {}


@app.get("/")
def homepage():
    """Show board."""

    return render_template("index.html")


@app.post("/api/new-game")
def new_game():
    """Start a new game and return JSON: {game_id, board}."""

    # get a unique string id for the board we're creating
    game_id = str(uuid4())
    game = BoggleGame()
    games[game_id] = game

    return jsonify({"gameId": game_id, "board": game.board})

@app.post("/api/score-word")
def score_word():
    """Accepts a POST request with JSON for gameID and word, returns
    JSON containing result -> {result: "ok"} / {result: "not-word"} / {result: "not-on-board"}
    """
    game = games[game_id]

    new_word = request.json.get("newWordForm")

    if game.is_word_in_word_list(self, new_word):
        if game.check_word_on_board(self, new_word) and game.is_word_not_a_dup(self, new_word):
            return jsonify({result: "ok"})
        else:
            return jsonify({result: "not-on-board"})
    else:
        return jsonify({result: "not-word"})
