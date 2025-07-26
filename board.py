# Author: Margaret Seymour
# GitHub username: seydev27
# Date: 2025-07-25
# Description: Handles board creation, placement, and visual representation for Troll Riddle Race.
# Manages a 7x7 grid with a player, troll, and treasure. Includes methods for movement and board display.

import random
from colorama import Fore, Style, init

# Initialize colorama for Windows compatibility
init(autoreset=True)


class Board:
    """
    Represents the 7x7 game grid and contains the logic for managing
    player, troll, and treasure positions, movement, and visual rendering.
    """

    def __init__(self, size=7):
        """
        Initializes the board with given size (default is 7x7).
        Randomly places the player (P), troll (T), and treasure ($).
        """
        self.size = size
        self.grid = [[' ' for _ in range(size)] for _ in range(size)]
        self.player_pos = self._get_random_empty_position()
        self.troll_pos = self._get_random_empty_position()
        self.treasure_pos = self._get_random_empty_position()
        self._update_board()

    def _get_random_empty_position(self):
        """Finds a random position on the board that is not occupied."""
        while True:
            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)
            if (row, col) not in [getattr(self, attr, None) for attr in ['player_pos', 'troll_pos', 'treasure_pos']]:
                return (row, col)

    def _update_board(self):
        """Clears and redraws the board with current entity positions."""
        self.grid = [[' ' for _ in range(self.size)] for _ in range(self.size)]
        pr, pc = self.player_pos
        tr, tc = self.troll_pos
        gr, gc = self.treasure_pos
        self.grid[pr][pc] = Fore.GREEN + 'P' + Style.RESET_ALL
        self.grid[tr][tc] = Fore.RED + 'T' + Style.RESET_ALL
        self.grid[gr][gc] = Fore.YELLOW + '$' + Style.RESET_ALL

    def display(self):
        """Prints the current state of the board."""
        print("\n   " + " ".join(str(i) for i in range(self.size)))
        for idx, row in enumerate(self.grid):
            print(f"{idx} |" + "|".join(row) + "|")

    def move_player(self, direction):
        """
        Moves the player one square in the given direction (N/S/E/W),
        if that move is within bounds.
        """
        dir_map = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}
        if direction.upper() not in dir_map:
            print("Invalid direction. Use N, S, E, or W.")
            return
        dr, dc = dir_map[direction.upper()]
        r, c = self.player_pos
        new_r, new_c = r + dr, c + dc
        if 0 <= new_r < self.size and 0 <= new_c < self.size:
            self.player_pos = (new_r, new_c)
            self._update_board()

    def move_troll(self):
        """
        Moves the troll one step toward the player or treasure.
        This is a simple heuristic that chooses whichever is closer.
        """
        targets = [self.player_pos, self.treasure_pos]
        tr, tc = self.troll_pos

        # Determine closest target
        distances = [abs(tr - r) + abs(tc - c) for r, c in targets]
        target = targets[distances.index(min(distances))]
        dr = target[0] - tr
        dc = target[1] - tc

        # Move in vertical or horizontal direction depending on distance
        new_r = tr + (1 if dr > 0 else -1 if dr < 0 else 0)
        new_c = tc + (1 if dc > 0 else -1 if dc < 0 else 0)

        if 0 <= new_r < self.size and 0 <= new_c < self.size:
            self.troll_pos = (new_r, new_c)
            self._update_board()

    def game_state(self):
        """
        Checks if the game has ended.
        Returns:
            "player_wins", "troll_wins", or "ongoing"
        """
        if self.player_pos == self.treasure_pos:
            return "player_wins"
        elif self.troll_pos == self.player_pos:
            return "troll_wins"
        return "ongoing"
