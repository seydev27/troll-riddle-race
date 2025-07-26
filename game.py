# Author: Margaret Seymour
# GitHub username: seydev27
# Date: 2025-07-25
# Description:
# Main gameplay loop for Troll Riddle Race. Controls flow of turns,
# riddles, and user decisions. Uses Board class and ask_riddle function.

from board import Board
from riddles import ask_riddle

def play_game():
    """
    Runs the full game loop for Troll Riddle Race.
    Presents a riddle each turn. If the player answers correctly,
    they choose a direction to move. Otherwise, the troll moves.
    Game ends if player finds the treasure or troll catches the player.
    """
    board = Board()

    print("\n🎮 Welcome to Troll Riddle Race!")
    print("Your goal: Reach the treasure before the troll catches you.")
    print("Answer riddles to move. If you miss... the troll moves instead.\n")

    while True:
        board.display()

        print("🧠 Riddle Challenge:")
        if ask_riddle():
            direction = input("✅ Correct! Choose a direction (N/S/E/W): ").strip().upper()
            moved = board.move_player(direction)

            if not moved:
                print("⚠️ Invalid move. That direction didn’t work. No action this turn.\n")
        else:
            print("❌ Incorrect! The troll takes a step...\n")
            target = board.move_troll()

            if target == "player":
                print("👣 You hear heavy footsteps behind you...\n")
            else:
                print("🗺 The troll bellows in the distance — maybe it’s after the treasure?\n")

        state = board.game_state()

        if state == "player_wins":
            board.display()
            print("🏆 You reached the treasure and outsmarted the troll!\n")
            break

        elif state == "troll_wins":
            board.display()
            print("💀 The troll caught you. Better luck next time!\n")
            break

if __name__ == "__main__":
    play_game()
