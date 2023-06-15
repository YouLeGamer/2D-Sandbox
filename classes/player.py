import pygame
import keyboard
import other.settings as settings

class Player:

    def __init__(self, args):
        self.screen = args[0]
        self.controls = settings.controls
        self.img_path = "placeholder"
        self.surface = pygame.image.load(self.img_path)
        self.scale = args[9]
        self.rect = pygame.rect.Rect((0, 0), (self.surface.get_size()[0]*self.scale, self.surface.get_size()[1]*self.scale))

        self.name = args[1]
        self.health = args[2]
        self.damage = args[3]
        self.mana = args[4]
        self.level = args[5]
        self.level = args[6]
        self.weapon = args[7]
        self.money = args[8]

        self.player_direction = None
        self.pos = (0, 0)
        self.pos = [350, 250]
        self.speed = 0.1

        self.clock = pygame.time.Clock()
        self.delta_time = self.clock.tick(60)


    def update(self):
        def update(self):
            self.rect = pygame.rect.Rect(self.pos, (self.surface.get_size()[0] * self.scale, self.surface.get_size()[1] * self.scale))

        self.player_direction = (
            keyboard.is_pressed(self.controls["right"]), keyboard.is_pressed(self.controls["left"]),
            keyboard.is_pressed(self.controls["jump"])
        )

        self.pos[0] += self.player_direction[0] * self.speed * self.delta_time
        self.pos[1] -= self.player_direction[1] * self.speed * self.delta_time

        # Scaling the player
        self.surface = pygame.transform.scale(self.surface, (
        self.surface.get_size()[0] * self.scale, self.surface.get_size()[1] * self.scale))
        self.screen.blit(self.surface, self.pos)