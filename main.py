import tkinter as tk
from constants import (
    WIDTH, HEIGHT, BACKGROUND_COLOR
)
from snake import Snake
from food import Food
from game import next_turn, change_direction

HIGHSCORE_FILE = "highscore.txt"

def load_high_score():
    try:
        with open(HIGHSCORE_FILE, "r") as f:
            return int(f.read())
    except (FileNotFoundError, ValueError):
        return 0

def save_high_score(score):
    with open(HIGHSCORE_FILE, "w") as f:
        f.write(str(score))

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Snake Game")
    window.resizable(False, False)

    high_score = load_high_score()

    game_state = {
        'score': 0,
        'high_score': high_score,
        'direction': 'down',
        'direction_locked': False
    }

    score_label = tk.Label(window, text=f"Score: {game_state['score']}", font=('consolas', 20))
    score_label.pack()

    high_score_frame = tk.Frame(window)
    high_score_frame.pack()

    high_score_label = tk.Label(high_score_frame, text=f"High Score: {game_state['high_score']}", font=('consolas', 20))
    high_score_label.pack(side=tk.LEFT)

    reset_button = tk.Button(high_score_frame, text='🔄', command=lambda: reset_high_score(), font=('consolas', 15), borderwidth=0)
    reset_button.pack(side=tk.LEFT)

    canvas = tk.Canvas(window, bg=BACKGROUND_COLOR, height=HEIGHT, width=WIDTH)
    canvas.pack()
    window.canvas = canvas

    window.update()

    window_width = window.winfo_width()
    window_height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width/2) - (window_width/2))
    y = int((screen_height/2) - (window_height/2))

    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    snake = None
    food = None

    def restart_game(event=None):
        global snake, food
        canvas.delete(tk.ALL)
        snake = Snake(canvas)
        food = Food(canvas, snake)
        game_state['score'] = 0
        game_state['direction'] = 'down'
        game_state['direction_locked'] = False
        score_label.config(text=f"Score: {game_state['score']}")
        next_turn(snake, food, window, score_label, game_state, high_score_label, save_high_score)

    def reset_high_score(event=None):
        game_state['high_score'] = 0
        save_high_score(0)
        high_score_label.config(text=f"High Score: {game_state['high_score']}")

    window.bind('<Left>', lambda event: change_direction('left', game_state))
    window.bind('<Right>', lambda event: change_direction('right', game_state))
    window.bind('<Up>', lambda event: change_direction('up', game_state))
    window.bind('<Down>', lambda event: change_direction('down', game_state))
    window.bind('r', restart_game)

    restart_game()
    window.mainloop()