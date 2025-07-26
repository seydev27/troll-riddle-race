# Author: Margaret Seymour  
# GitHub username: seydev27  
# Date: 2025-07-25  
# Description: Main game loop for Troll Riddle Race.  
# Coordinates gameplay, movement logic, and riddle integration.  

import random
from board import create_board, display_board, move_entity, get_random_empty_position, distance
from riddles import ask_riddle, final_riddle_challenge

def get_player_move():
    """
    Prompts the player for a move direction and validates it.
    Returns one of: 'n', 's', 'e', 'w'
    """
    directions = {'n': (-1, 0), 's': (1, 0), 'e': (0, 1), 'w': (0, -1)}
    while True:
        move = input("Which direction do you want to move? (N/S/E/W): ").lower()
        if move in directions:
            return move
        print("Invalid direction. Try again.")

def move_troll(board, troll_pos, player_pos, treasure_pos):
    """
    Determines troll's move (towards player or treasure randomly) and updates the board.
    """
    target = player_pos if random.choice([True, False]) else treasure_pos
    hint = (
        "👣 You hear heavy footsteps... are they coming for YOU?"
        if target == player_pos else
        "💰 The troll bellows in the distance — maybe it’s after the TREASURE?"
    )
    print(f"\n{hint}")

    troll_r, troll_c = troll_pos
    target_r, target_c = target
    new_r = troll_r + (1 if target_r > troll_r else -1 if target_r < troll_r else 0)
    new_c = troll_c + (1 if target_c > troll_c else -1 if target_c < troll_c else 0)

    return move_entity(board, troll_pos, (new_r, new_c), "T")

def game_loop():
    """
    Main game logic: initializes board and handles turn-based player vs troll movement.
    """
    board = create_board(7, 7)

    player_pos = get_random_empty_position(board)
    board[player_pos[0]][player_pos[1]] = "P"

    troll_pos = get_random_empty_position(board)
    board[troll_pos[0]][troll_pos[1]] = "T"

    treasure_pos = get_random_empty_position(board)
    board[treasure_pos[0]][treasure_pos[1]] = "💰"

    print("🎮 Welcome to Troll Riddle Race!")
    print("Solve riddles to move. If you fail, the troll moves instead!")
    print("Reach the treasure before the troll catches you!")
    
    while True:
        display_board(board)

        if player_pos == treasure_pos:
            print("🏁 You've reached the treasure! Solve this final riddle to win:")
            if final_riddle_challenge():
                print("🏆 You win!")
            else:
                print("💀 The troll caught you during the challenge. Game over.")
            break

        if player_pos == troll_pos:
            print("💀 The troll caught you! Game over.")
            break

        if ask_riddle():
            print("✅ Correct! You may move.")
            direction = get_player_move()
            delta = {'n': (-1, 0), 's': (1, 0), 'e': (0, 1), 'w': (0, -1)}
            d_row, d_col = delta[direction]
            new_pos = (player_pos[0] + d_row, player_pos[1] + d_col)
            player_pos = move_entity(board, player_pos, new_pos, "P")
        else:
            print("❌ Wrong answer. The troll moves!")
            troll_pos = move_troll(board, troll_pos, player_pos, treasure_pos)

if __name__ == "__main__":
    game_loop()
