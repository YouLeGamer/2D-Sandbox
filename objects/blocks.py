import pygame


class Block:

    def __init__(self, texture_path, scale, pos, breaking_time, is_usable, has_random_drop, drop, tool_requirement,
                 any_requirement, collision_rect):
        self.texture_path = texture_path
        self.surface = pygame.surface.Surface(self.texture_path)
        self.scale = scale
        self.pos = pos
        self.breaking_time = breaking_time
        self.is_usable = is_usable
        self.has_random_drop = has_random_drop
        self.drop = drop
        self.tool_requirement = tool_requirement
        self.any_requirement = any_requirement
        self.collision_rect = collision_rect
