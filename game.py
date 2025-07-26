# Author: Margaret Seymour
# GitHub username: seydev27
# Date: 2025-07-25
# Description:
# This is the main control file for Troll Riddle Race.
# It manages player input, turn logic, and win/loss outcomes using recursion,
# 2D grid navigation, and modular code from board and riddles modules.

from board import Board
from riddles import ask_riddle

def play_game():
    """
    This function starts and runs the main game loop.

    How the game works:
    - The player and troll begin at random locations on a grid.
    - Each turn presents a riddle to the player.
        • If answered correctly, the player chooses a direction to move.
        • If answered incorrectly, the troll moves.
    - The game ends when either:
        • The player reaches the treasure (win)
        • The troll reaches the player (loss)

    This function demonstrates:
    - Recursive question handling (via ask_riddle)
    - Modular logic separation (via Board class)
    - Grid-based movement using 2D position tracking
    """
    board = Board()  # Create a new game board with randomized start positions

    print("\n🎮 Welcome to Troll Riddle Race!")
    print("Solve riddles to move. Miss one, and the troll gets a step closer!")
    print("Can you reach the treasure before it reaches you?\n")

    while True:
        board.display()  # Show current state of the board

        print("🧠 Riddle Challenge:")
        if ask_riddle():  # This is a recursive function that evaluates a riddle
            direction = input("✅ Correct! Choose a direction (N/S/E/W): ").strip().upper()
            moved = board.move_player(direction)

            if not moved:
                print("⚠️ Invalid move. That direction didn’t work. No action this turn.\n")
        else:
            print("❌ Incorrect! The troll takes a step...\n")
            board.move_troll()

        state = board.game_state()

        if state == "player_wins":
            board.display()
            print("🏆 Congratulations! You reached the treasure and outsmarted the troll!\n")
            break

        elif state == "troll_wins":
            board.display()
            print("💀 The troll has caught you. Better luck next time...\n")
            break

# Only run the game loop if this file is executed directly
if __name__ == "__main__":
    play_game()
