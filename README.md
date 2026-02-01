# Snake Game 🐍

A classic Snake game built with **Python** using the **Turtle graphics module**.  
The player controls a growing snake, collects food, and tries to achieve the highest score.

## Features
- Snake movement controlled by keyboard
- Snake grows when food is eaten
- Score and high score tracking
- High score saved to a text file
- Game over when the snake hits the wall or itself

## Technologies Used
- Python
- Turtle module

## How to Run
Run the main game file:

```bash
python snake_game.py
```

## How It Works
1.The game window is created using the Turtle module
2.The snake moves continuously on the screen
3.Each time the snake eats food:
  -the snake grows longer
  -the score increases
4.If the snake hits the wall or its own body, the game ends
5.The highest score is saved to a text file and loaded when the game restarts

## Data Storage
-The current score is tracked during gameplay
-The high score is stored locally in a text file

## Notes
This project was created for learning purposes and to practice game logic using Python.
