import pgzrun
from random import randint

TITLE = 'Flappy Ball'
WIDTH = 800
HEIGHT = 600

# Define random colors for both balls
R1, G1, B1 = randint(0, 255), randint(0, 255), randint(0, 255)
CLR1 = R1, G1, B1

R2, G2, B2 = randint(0, 255), randint(0, 255), randint(0, 255)
CLR2 = R2, G2, B2

GRAVITY = 2000.0  # pixels per second per second

class Ball:
    def __init__(self, initial_x, initial_y, vx, vy, color):
        self.x = initial_x
        self.y = initial_y
        self.vx = vx
        self.vy = vy
        self.radius = 40
        self.color = color

    def draw(self):
        pos = (self.x, self.y)
        screen.draw.filled_circle(pos, self.radius, self.color)

# Create two balls with different velocities and colors
ball1 = Ball(50, 100, 200, 0, CLR1)
ball2 = Ball(200, 300, 150, 0, CLR2)

def draw():
    screen.clear()
    ball1.draw()
    ball2.draw()

def update(dt):
    # Apply constant acceleration to both balls
    for ball in [ball1, ball2]:
        uy = ball.vy
        ball.vy += GRAVITY * dt
        ball.y += (uy + ball.vy) * 0.5 * dt
        
        # Detect and handle bounce
        if ball.y > HEIGHT - ball.radius:
            ball.y = HEIGHT - ball.radius
            ball.vy = -ball.vy * 0.9  # inelastic collision
        
        # X component doesn't have acceleration
        ball.x += ball.vx * dt
        
        if ball.x > WIDTH - ball.radius or ball.x < ball.radius:
            ball.vx = -ball.vx

def on_key_down(key):
    """Pressing a key will kick both balls upwards."""
    if key == keys.SPACE:
        ball1.vy = -500
        ball2.vy = -700  # Different force for the second ball

pgzrun.go()
