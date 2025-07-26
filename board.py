# Author: Margaret Seymour
# GitHub username: seydev27
# Date: 2025-07-25
# Description:
# This module manages the 7x7 board for Troll Riddle Race. It tracks
# the player, troll, and treasure on a grid. It also handles movement logic,
# board rendering, and win/loss condition checks.

import random
from colorama import Fore, Style, init

init(autoreset=True)

class Board:
    """
    Represents the 7x7 game grid and logic for managing the game state.
    """

    def __init__(self, size=7):
        """
        Initializes the board, places player, troll, and treasure in random cells.
        """
        self.size = size
        self.grid = [[' ' for _ in range(size)] for _ in range(size)]
        self.player_pos = self._get_random_empty_position()
        self.troll_pos = self._get_random_empty_position()
        self.treasure_pos = self._get_random_empty_position()
        self._update_board()

    def _get_random_empty_position(self):
        """Returns a random unoccupied position on the board."""
        while True:
            r = random.randint(0, self.size - 1)
            c = random.randint(0, self.size - 1)
            if (r, c) not in [getattr(self, attr, None) for attr in ['player_pos', 'troll_pos', 'treasure_pos']]:
                return (r, c)

    def _update_board(self):
        """Updates the grid to reflect current positions of all entities."""
        self.grid = [[' ' for _ in range(self.size)] for _ in range(self.size)]
        pr, pc = self.player_pos
        tr, tc = self.troll_pos
        gr, gc = self.treasure_pos
        self.grid[pr][pc] = Fore.GREEN + 'P' + Style.RESET_ALL
        self.grid[tr][tc] = Fore.RED + 'T' + Style.RESET_ALL
        self.grid[gr][gc] = Fore.YELLOW + '$' + Style.RESET_ALL

    def display(self):
        """Displays the current grid to the console."""
        print("\n   " + " ".join(str(i) for i in range(self.size)))
        for idx, row in enumerate(self.grid):
            print(f"{idx} |" + "|".join(row) + "|")

    def move_player(self, direction):
        """
        Attempts to move the player one cell in the given direction.
        Valid inputs: 'N', 'S', 'E', 'W'.
        Returns True if move was successful, False if invalid.
        """
        dir_map = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}
        if direction.upper() not in dir_map:
            return False

        dr, dc = dir_map[direction.upper()]
        r, c = self.player_pos
        new_r, new_c = r + dr, c + dc

        if 0 <= new_r < self.size and 0 <= new_c < self.size:
            self.player_pos = (new_r, new_c)
            self._update_board()
            return True

        return False

    def move_troll(self):
        """
        Moves the troll one step toward the nearest target (player or treasure).
        Returns "player" or "treasure" to indicate who it’s chasing.
        """
        targets = [self.player_pos, self.treasure_pos]
        tr, tc = self.troll_pos

        # Determine closest target
        distances = [abs(tr - r) + abs(tc - c) for r, c in targets]
        target_index = distances.index(min(distances))
        target = targets[target_index]
        target_type = "player" if target_index == 0 else "treasure"

        # Move one step toward the target
        dr = target[0] - tr
        dc = target[1] - tc
        new_r = tr + (1 if dr > 0 else -1 if dr < 0 else 0)
        new_c = tc + (1 if dc > 0 else -1 if dc < 0 else 0)

        if 0 <= new_r < self.size and 0 <= new_c < self.size:
            self.troll_pos = (new_r, new_c)
            self._update_board()

        return target_type

    def game_state(self):
        """
        Checks win/loss conditions.
        Returns:
            "player_wins", "troll_wins", or "ongoing"
        """
        if self.player_pos == self.treasure_pos:
            return "player_wins"
        elif self.troll_pos == self.player_pos:
            return "troll_wins"
        return "ongoing"
