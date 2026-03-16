from os import name
import pygame
from config import *
from game.player import Player
from game.platform import Platform
from game.coin import Coin
from random import randint


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True

        self.all_sprites = pygame.sprite.Group()
        self.platform = pygame.sprite.Group()

        self.player = Player(50, 500)
        self.all_sprites.add(self.player)

        self.font = pygame.font.SysFont(None, 30)

        self.coins = pygame.sprite.Group()

        ground = Platform(0, SCREEN_HEIGHT - 40, SCREEN_WIDTH, 40)
        self.platform.add(ground)
        self.all_sprites.add(ground)

        platform1 = Platform(450, 400, 300, 10)
        self.platform.add(platform1)
        self.all_sprites.add(platform1)

        platform2 = Platform(50, 300, 200, 10)
        self.platform.add(platform2)
        self.all_sprites.add(platform2)

        coin1 = Coin(randint(10, SCREEN_WIDTH - 10), randint(10, 100), *COIN_SIZE)
        self.coins.add(coin1)
        self.all_sprites.add(coin1)

        coin2 = Coin(randint(10, SCREEN_WIDTH - 10), randint(200, 300), *COIN_SIZE)
        self.coins.add(coin2)
        self.all_sprites.add(coin2)

        coin3 = Coin(randint(10, SCREEN_WIDTH - 10), randint(400, 500), *COIN_SIZE)
        self.coins.add(coin3)
        self.all_sprites.add(coin3)

    def handle_events(self):
        for event in pygame.event.get():
            evt_name = pygame.event.event_name(event.type)

            if event.type == pygame.QUIT:
                self.running = False

            if event.type in (pygame.KEYDOWN, pygame.KEYUP):
                evt_key = pygame.key.name(event.key)
                print(f"{evt_name}: {evt_key}")

            elif event.type == pygame.MOUSEMOTION:
                print(f"{evt_name}: {event.pos}")

            elif event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP):
                print(f"{evt_name}: {event.button} at {event.pos}")
    
    def update(self):
        hits = pygame.sprite.spritecollide(self.player, self.coins, dokill=True)
        for _ in hits:
            self.player.add_score(1)

        game_over = self.player.update(self.platform)
        if game_over:
            self.running = False

    def draw(self):
        self.screen.fill(SKY_BLUE)
        
        for sprite in self.all_sprites:
            sprite.draw(self.screen)

        # citac skore
        score_surf = self.font.render(f"pocet penizku: {self.player.score}", True, (0, 0, 0))
        score_rect = score_surf.get_rect()
        score_rect.topright = (SCREEN_WIDTH - 10, 10)
        self.screen.blit(score_surf, score_rect)
        if self.player.score == 3:
            print("Vyhral si!")
            pygame.time.delay(1000)
            self.running = False

        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)