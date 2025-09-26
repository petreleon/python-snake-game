import random
from constants import WIDTH, HEIGHT, SPACE_SIZE, FOOD_COLOR

class Food:
    def __init__(self, canvas):
        self.canvas = canvas
        x = random.randint(0, (WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]
        self.canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")
