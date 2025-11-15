# API endpoints for moves, new game, etc.

from flask import Blueprint, request, jsonify
from game.game_manager import GameManager
from game.player import Player
from game.ai.random_ai import RandomAI

game_routes = Blueprint("game_routes", __name__)

# Global game (later you can support multi-session or DB storage)
game = None

@game_routes.post("/new")
def new_game():
    global game

    p1 = Player("Player")
    ai = Player("AI", is_ai=True, ai_controller=RandomAI())

    game = GameManager(p1, ai)

    return jsonify({"status": "new_game_started"})


@game_routes.post("/move")
def move():
    global game
    data = request.json

    x = data.get("x")
    y = data.get("y")

    result = game.make_move(x, y)

    return jsonify(result)

