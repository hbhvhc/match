import pygame
import random
import sys


pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.SysFont("Arial", 40)
FPS = 60

ARROW_KEYS = {
    "left": pygame.K_LEFT,
    "right": pygame.K_RIGHT,
    "up": pygame.K_UP,
    "down": pygame.K_DOWN
}

ARROW_SYMBOLS = {
    "left": "←",
    "right": "→",
    "up": "↑",
    "down": "↓"
}


class Arrow:
    def __init__(self, direction, x, y):
        self.direction = direction
        self.x = x
        self.y = y
        self.speed = 5

    def draw(self, screen):
        arrow_surface = FONT.render(ARROW_SYMBOLS[self.direction], True, WHITE)
        screen.blit(arrow_surface, (self.x, self.y))

    def update(self):
        self.y += self.speed


def game_loop():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Rhythm Game")

    clock = pygame.time.Clock()
    score = 0

    arrows = []
    spawn_delay = 1500  # ms
    last_spawn_time = pygame.time.get_ticks()

    game_over = False

    while not game_over:
        screen.fill(BLACK)

        #input handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #make the arrows
        current_time = pygame.time.get_ticks()
        if current_time - last_spawn_time > spawn_delay:
            direction = random.choice(list(ARROW_KEYS.keys()))
            x_position = {"left": 150, "up": 250, "down": 350, "right": 450}[direction]
            arrows.append(Arrow(direction, x_position, -50))
            last_spawn_time = current_time

        for arrow in arrows[:]:
            arrow.update()
            arrow.draw(screen)

          
            if arrow.y > SCREEN_HEIGHT - 100:
                arrows.remove(arrow)
                game_over = True  

      
        keys = pygame.key.get_pressed()
        for arrow in arrows[:]:
            if SCREEN_HEIGHT - 150 < arrow.y < SCREEN_HEIGHT - 50:
                if keys[ARROW_KEYS[arrow.direction]]:
                    arrows.remove(arrow)
                    score += 10

       
        score_surface = FONT.render(f"Score: {score}", True, WHITE)
        screen.blit(score_surface, (10, 10))

        
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    game_loop()
