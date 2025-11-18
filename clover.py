import pygame
import random as r

class Clover(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, maxspeed, color):
        super().__init__()
        self.x = x
        self.y = y
        self.screen = screen
        self.speed = r.randint(1, maxspeed)
        self.color = color

        try:
            self.img = pygame.image.load("assets/clover.png")
            print("clover.png loaded successfully")
        except Exception as e:
            print("Clover image load failed:", e)
            self.img = pygame.Surface((50, 50))
            self.img.fill((0, 255, 0))  # fallback green box

        self.rect = pygame.Rect(self.x, self.y, self.img.get_width(), self.img.get_height())

    def update(self):
        self.screen.blit(self.img, (self.x, self.y))
        self.y += self.speed
        self.rect.y = self.y