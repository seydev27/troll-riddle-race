# Author: Margaret Seymour
# GitHub username: seydev27
# Date: 2025-07-25
# Description:
# Riddle library module for Troll Riddle Race.
# Contains a bank of (question, answer) pairs and the main riddle function.
# Used by the game to test player logic and control turn flow.

import random

# List of 20 riddle (question, answer) pairs
RIDDLES = [
    ("What has keys but can't open locks?", "piano"),
    ("What has hands but can’t clap?", "clock"),
    ("What gets wetter as it dries?", "towel"),
    ("What has to be broken before you can use it?", "egg"),
    ("I’m tall when I’m young and short when I’m old. What am I?", "candle"),
    ("What has a neck but no head?", "bottle"),
    ("What goes up but never comes down?", "age"),
    ("What has one eye but can’t see?", "needle"),
    ("What can travel around the world while staying in the same spot?", "stamp"),
    ("What has legs but doesn’t walk?", "table"),
    ("The more you take, the more you leave behind. What are they?", "footsteps"),
    ("What comes once in a minute, twice in a moment, but never in a thousand years?", "m"),
    ("What is full of holes but still holds water?", "sponge"),
    ("What is so fragile that saying its name breaks it?", "silence"),
    ("What can you catch but not throw?", "cold"),
    ("What has a head and a tail but no body?", "coin"),
    ("What has cities but no houses, forests but no trees, and water but no fish?", "map"),
    ("What invention lets you look right through a wall?", "window"),
    ("What has many teeth but can’t bite?", "comb"),
    ("What begins with T, ends with T, and has T in it?", "teapot")
]

def ask_riddle():
    """
    Selects a random riddle from the list and asks the player to solve it.
    Returns True if the player's answer is correct, False otherwise.
    """
    question, answer = random.choice(RIDDLES)
    print(f"\n🔍 Riddle: {question}")
    user_response = input("Your answer: ").strip().lower()

    return user_response == answer.lower()
