import random
from constants import WIDTH, HEIGHT, SPACE_SIZE, FOOD_COLOR

class Food:
    def __init__(self, canvas, snake):
        self.canvas = canvas
        while True:
            x = random.randint(0, (WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
            y = random.randint(0, (HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
            # Ensure food does not spawn on the snake
            on_snake = False
            for part in snake.coordinates:
                if x == part[0] and y == part[1]:
                    on_snake = True
                    break
            if not on_snake:
                break
        self.coordinates = [x, y]
        self.canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")
