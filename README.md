# 🧌 Troll Riddle Race

Troll Riddle Race is a modular, Python-based puzzle game where you race a troll across a grid — one riddle at a time.

I built it to sharpen my Python skills while studying Python, using recursion, logic, and modular programming — with a twist: a custom riddle library.

---
**🎯 Project Objective**

This game was designed as a creative way to reinforce core computer science concepts.

Skills practiced:

🧠 Logic & problem-solving through riddle-based progression
🔁 Recursion, especially in the final multi-attempt riddle mechanic
🗺️ Grid navigation and state tracking with 2D coordinates
📦 Python library use, like colorama for UI enhancement
🧩 Clean, modular code design using reusable components

---
**🎯 Goal: Solve riddles to reach the treasure before the troll does — and avoid getting caught!**

**🧠 How to Play** 
The gameplay occurs on a 7×7 grid. You, the troll, and the treasure all begin in random squares. Each turn updates the grid to track your position.


🕹️ Gameplay
1. A riddle is presented to you.
2. ✅ Correct answer?
   You choose a direction and move one step: N, S, E, or W.
3. ❌ Incorrect answer?
   The troll moves one step instead.
4. ⚠️ Beware:
   The troll might be chasing you or heading for the treasure — you get a hint each turn:
      “You hear heavy footsteps... are they coming for you?” 😬
      “The troll bellows in the distance — maybe it’s after the treasure?” 💰
5. Reach the treasure first — or get caught trying.
6. Once at the treasure:
   You get 3 chances per turn to solve the final riddle.
   If you succeed...
   **🏆 YOU WIN!**
7. But if the troll catches you first?
   💀 GAME OVER.

---

💡 Technologies Used

Python 3.x
CLI-based interaction
colorama for optional text styling

---
Reqs

Python 3.x
colorama  # optional
