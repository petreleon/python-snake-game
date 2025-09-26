# Snake Game

A classic Snake game implemented in Python using the `tkinter` library.

## Features

- Classic Snake gameplay: control a snake to eat food and grow longer.
- Game over when the snake hits the wall or itself.
- Score and High Score tracking.
- Persistent high score saved in `highscore.txt`.
- Restart the game after a game over.
- Reset the high score with the click of a button.

## Screenshot

![image](https://github.com/user-attachments/assets/15238a6b-1a5c-42e6-9386-311358c31b3a)


## Requirements

- Python 3
- `tkinter` library (usually included with Python, but may need to be installed separately on some systems).

## How to Run

1.  Make sure you have Python 3 and `tkinter` installed.
2.  Download all the `.py` files.
3.  Open a terminal in the directory where you saved the files.
4.  Run the game with the following command:

    ```bash
    python3 main.py
    ```

## Controls

-   **Arrow Keys:** Control the direction of the snake.
-   **'r' key:** Restart the game after a game over.
-   **🔄 button:** Reset the high score to 0.

## File Structure

The project is organized into the following files:

-   `main.py`: The main entry point for the application. Handles window creation, game state, and user input.
-   `snake.py`: Contains the `Snake` class.
-   `food.py`: Contains the `Food` class.
-   `game.py`: Contains the core game logic functions.
-   `constants.py`: Contains all the constant values for the game.
-   `highscore.txt`: Stores the high score.
