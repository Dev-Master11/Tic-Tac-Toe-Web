from flask import Flask, render_template, request, jsonify, session
import random

app = Flask(__name__)
app.secret_key = "tic_tac_toe_secret"

def initialize_board():
    return [' '] * 10

def win_check(board, choice):
    win_combinations = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Columns
        [1, 5, 9], [3, 5, 7]              # Diagonals
    ]
    return any(all(board[pos] == choice for pos in combo) for combo in win_combinations)

def full_board_check(board):
    return all(space != ' ' for space in board[1:])

def computer_choice(board):
    available_positions = [pos for pos in range(1, 10) if board[pos] == ' ']
    return random.choice(available_positions) if available_positions else None

@app.route("/")
def home():
    session["board"] = initialize_board()
    session["player"] = "X"
    session["winner"] = None
    return render_template("index.html")

@app.route("/play", methods=["POST"])
def play():
    data = request.json
    board = session.get("board", initialize_board())
    player = session.get("player", "X")
    winner = session.get("winner", None)

    if winner is None and board[data["position"]] == " ":
        board[data["position"]] = player
        if win_check(board, player):
            session["winner"] = f"{player} wins!"
        elif full_board_check(board):
            session["winner"] = "It's a draw!"
        else:
            session["player"] = "O" if player == "X" else "X"

            # If it's the computer's turn, make a move
            if session["player"] == "O":
                comp_pos = computer_choice(board)
                if comp_pos:
                    board[comp_pos] = "O"
                    if win_check(board, "O"):
                        session["winner"] = "Computer wins!"
                    elif full_board_check(board):
                        session["winner"] = "It's a draw!"
                    else:
                        session["player"] = "X"

    session["board"] = board
    return jsonify({"board": board, "player": session["player"], "winner": session["winner"]})

@app.route("/reset", methods=["POST"])
def reset():
    session.clear()
    return jsonify({"message": "Game reset!"})

if __name__ == "__main__":
    app.run(debug=True)
