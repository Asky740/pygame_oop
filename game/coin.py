import pygame
import os
from config import *

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))

        image_loaded = False

        for name in ["coin"]:
            for ext in ["png", "jpg", "jpeg", "webp"]:
                try:
                    image_path = os.path.join("img", f"{name}.{ext}")
                    self.image = pygame.image.load(image_path).convert_alpha()
                    self.image = pygame.transform.scale(self.image, (COIN_SIZE))
                    print(f"Načten obrázek mince: {image_path}")
                    image_loaded = True

                    break
                
                except (pygame.error, FileNotFoundError):
                    print(f"Coin nebyl nalezen {pygame.error}")
                    continue
        
        if not image_loaded:
            self.image = pygame.Surface(COIN_SIZE)
            self.image.fill(PLATFORM_COLOR)
            
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.image, self.rect)