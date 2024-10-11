# Breakout Game in Python

This project is a simple implementation of the classic Breakout game using Python's Turtle graphics library. Players control a paddle to bounce a ball and break bricks. The game includes features like scoring and lives.

## Features

- **Paddle Control**: Move the paddle left and right to bounce the ball.
- **Bricks**: Multiple rows of bricks that disappear when hit by the ball.
- **Score Tracking**: Keep track of the player's score based on the number of bricks destroyed.
- **Lives**: The player has three lives; the game ends when all lives are lost.
- **Winning Condition**: The game ends when all bricks are destroyed.

## How to Play

1. Clone this repository to your local machine.
2. Ensure you have Python installed (preferably Python 3).
3. Run `main.py` to start the game.
4. Use the left and right arrow keys to move the paddle.
5. Try to break all the bricks without letting the ball fall past the paddle!

## Files

- `main.py`: The main game loop and game logic.
- `ball.py`: Contains the `Ball` class to manage the ball's behavior.
- `paddle.py`: Contains the `Paddle` class to control the paddle.
- `brick.py`: Contains the `Brick` class for the bricks in the game.

## Requirements

- Python 3.x
- Turtle graphics library (comes with Python by default)

## License

This project is part of Angela Yu's 100 Days of Code course and is meant for educational purposes. Feel free to modify and improve the code.
