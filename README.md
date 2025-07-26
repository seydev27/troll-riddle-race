# 🧌 Troll Riddle Race

**Troll Riddle Race** is a modular, Python-based logic game built as a final project to apply key programming skills from CS162. Players navigate a grid by solving riddles, racing against a troll to reach a hidden treasure — with recursion, randomness, and risk at every turn.

---

## 🎯 Overview

### 🧠 Python concepts practiced:
- **Recursion** – used in the final treasure challenge logic
- **Conditionals and control flow** – in player/troll decisions and movement
- **2D list/grid navigation** – with positional updates and collision checking
- **Modular design** – separate files for game logic, board, and riddles
- **Randomization** – for entity placement and riddle selection
- **User input validation** – direction control and answer checking
- **Optional color styling** – with `colorama` for terminal highlights

---

## 🕹️ How to Play

The game is played on a 7×7 grid. 
You, the troll, and the treasure start in random empty squares.

Each round:
1. 🧩 You are asked a riddle.
2. ✅ If you answer correctly, you get to move (N/S/E/W).
3. ❌ If you answer incorrectly, the **troll** moves instead.
4. WARNING: The troll may pursue **you** or **the treasure**
   You see a hint:
   - *“You hear heavy footsteps... are they coming for you?”*
   - *“The troll bellows in the distance — maybe it’s after the treasure?”*

---

### 💰 The Endgame

- Reach the treasure first? You must solve one final riddle.
- You get **3 recursive chances** (no loops used).
- Solve it? **🏆 You win.**
- Fail it — or get caught by the troll? ** Game over.**

---

## 🛠 Technologies Used

- **Python 3.x**
- CLI-based interaction
- `colorama` *(optional)* – for enhanced text styling

---

## 📂 File Structure
📁 troll-riddle-race/
├── game.py # Main game loop and control
├── board.py # Grid creation, movement, and state handling
├── riddles.py # Riddle logic and recursive challenge
└── README.md # This file

---

Enjoy the race — and watch out for the troll. 💀💰🧌
