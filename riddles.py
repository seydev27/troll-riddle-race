# Author: Margaret Seymour
# GitHub username: seydev27
# Date: 2025-07-25
# Description: Riddle library for Troll Riddle Race.
#              Returns one random riddle as a (question, answer) tuple.
#              Riddles are wordplay or logic-based and intended for general audiences.

import random

def get_riddle():
    """
    Returns a random riddle from the 20 item list as a tuple (question, answer).
    The answer is always in lowercase for easier comparison.
    """
    riddles = [
        ("What has to be broken before you can use it?", "egg"),
        ("I’m tall when I’m young and short when I’m old. What am I?", "candle"),
        ("The more of me you take, the more you leave behind. What am I?", "footsteps"),
        ("What gets wetter the more it dries?", "towel"),
        ("What month has 28 days?", "all"),
        ("What comes once in a minute, twice in a moment, but never in a thousand years?", "m"),
        ("What begins with T, ends with T, and has T in it?", "teapot"),
        ("What has many keys but can’t open a lock?", "piano"),
        ("What can you catch but not throw?", "cold"),
        ("What has hands but can’t clap?", "clock"),
        ("What has words but never speaks?", "book"),
        ("What has one eye but can’t see?", "needle"),
        ("Forward I am heavy, but backward I am not. What am I?", "ton"),
        ("What has legs but doesn’t walk?", "table"),
        ("You see me once in June, twice in November, but not at all in May. What am I?", "e"),
        ("What has a neck but no head?", "bottle"),
        ("What goes up but never comes down?", "age"),
        ("What can travel around the world while staying in the same corner?", "stamp"),
        ("What kind of band never plays music?", "rubber"),
        ("What building has the most stories?", "library")
    ]
    return random.choice(riddles)
