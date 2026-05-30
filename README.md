#Snake Game

A classic Snake Game built with Python and Pygame where you control a snake, eat food to grow longer, and try to beat your high score without hitting the walls or yourself.

---

## Gameplay Preview

```
🟩 = Snake
🟥 = Food
⬛ = Background
```



## Features

- **Smooth Controls** — Use arrow keys to move the snake in all four directions.
- **Live Score** — Score is displayed in real time on the top left of the screen.
- **Food Spawning** — Food appears at a random position every time the snake eats it.
- **Collision Detection** — Game ends when the snake hits a wall or bites itself.
- **Game Over Screen** — Displays a "GAME OVER" message for 3 seconds before closing.

---

## How to Play

| Key | Action |
|---|---|
| ⬆️ Arrow Up | Move Up |
| ⬇️ Arrow Down | Move Down |
| ⬅️ Arrow Left | Move Left |
| ➡️ Arrow Right | Move Right |

- Every time the snake eats the **red food**, it grows longer and your **score increases by 1**
- Avoid hitting the **walls** or the **snake's own body**
- Try to get the highest score possible!

---

## How It Works

1. **Initialization** — Pygame is set up with a 600x600 screen and a grid cell size of 20px.
2. **Snake Movement** — The snake moves by inserting a new head in the current direction and removing the tail each frame.
3. **Food Logic** — When the snake's head position matches the food position, score increases and new food spawns at a random grid position.
4. **Collision Detection** — Checks if the new head goes out of bounds (wall collision) or overlaps with any body segment (self collision).
5. **Game Loop** — Runs at **10 FPS** using Pygame's clock, keeping the game speed consistent.
6. **Game Over** — When a collision is detected, the loop breaks and a Game Over screen is shown for 3 seconds.

---

## Tech Stack

| Technology | Purpose |
|---|---|
| **Python** | Core programming language |
| **Pygame** | Game rendering, input handling, and display |

---

## Installation

Make sure you have **Python 3.x** installed, then install Pygame:

```bash
pip install pygame
```

---

## Run the Game

```bash
python snake.py
```

---

## Project Structure

```bash
project/
│
├── snake.py       # Main game file with all logic
└── README.md      # Project documentation
```

---

## Future Improvements

- **High Score System** — Save and display the best score across sessions.
- **Difficulty Levels** — Easy, Medium, Hard modes with different speeds.
- **Sound Effects** — Add sounds for eating food and game over.
- **Colorful UI** — Add gradient snake, animated food, and a better game over screen.
- **Pause Feature** — Allow pausing and resuming the game mid-play.

---

## Author

**Rahul Kundu**