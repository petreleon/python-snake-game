import tkinter as tk
from constants import (
    WIDTH, HEIGHT, SPACE_SIZE, SPEED, SNAKE_COLOR
)

def next_turn(snake, food, window, score_label, game_state, high_score_label, save_high_score_func):
    x, y = snake.coordinates[0]

    if game_state['direction'] == "up":
        y -= SPACE_SIZE
    elif game_state['direction'] == "down":
        y += SPACE_SIZE
    elif game_state['direction'] == "left":
        x -= SPACE_SIZE
    elif game_state['direction'] == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, [x, y])
    square = window.canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        game_state['score'] += 1
        score_label.config(text=f"Score: {game_state['score']}")
        window.canvas.delete("food")
        food.__init__(window.canvas, snake)
    else:
        del snake.coordinates[-1]
        window.canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over(window, game_state, high_score_label, save_high_score_func)
    else:
        game_state['direction_locked'] = False
        window.after(SPEED, lambda: next_turn(snake, food, window, score_label, game_state, high_score_label, save_high_score_func))

def change_direction(new_direction, game_state):
    if game_state['direction_locked']:
        return

    if new_direction == 'left':
        if game_state['direction'] != 'right':
            game_state['direction'] = new_direction
            game_state['direction_locked'] = True
    elif new_direction == 'right':
        if game_state['direction'] != 'left':
            game_state['direction'] = new_direction
            game_state['direction_locked'] = True
    elif new_direction == 'up':
        if game_state['direction'] != 'down':
            game_state['direction'] = new_direction
            game_state['direction_locked'] = True
    elif new_direction == 'down':
        if game_state['direction'] != 'up':
            game_state['direction'] = new_direction
            game_state['direction_locked'] = True

def check_collisions(snake):
    x, y = snake.coordinates[0]
    if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
        return True
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
    return False

def game_over(window, game_state, high_score_label, save_high_score_func):
    if game_state['score'] > game_state['high_score']:
        game_state['high_score'] = game_state['score']
        save_high_score_func(game_state['high_score'])
        high_score_label.config(text=f"High Score: {game_state['high_score']}")

    window.canvas.delete(tk.ALL)
    window.canvas.create_text(window.canvas.winfo_width()/2, window.canvas.winfo_height()/2,
                   font=('consolas', 70), text="GAME OVER", fill="red", tag="gameover")
    window.canvas.create_text(window.canvas.winfo_width()/2, window.canvas.winfo_height()/2 + 70,
                   font=('consolas', 20), text="Press 'r' to restart", fill="white", tag="restart")
