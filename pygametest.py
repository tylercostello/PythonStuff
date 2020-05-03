import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Movement test')
FPSCLOCK = pygame.time.Clock()
FPS = 30

def main():
    done = False
    x = 0
    speed = 180 # Pixels per second.
    dt = FPSCLOCK.tick(60)/1000.0
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        x += speed*dt
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (0, 0, 255), (x, 300, 70, 80))
        pygame.display.flip()
        dt = FPSCLOCK.tick(FPS)/1000.0

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
