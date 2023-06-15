import pygame

class Advancements:

    def __init__(self, adv_name, adv_reward, adv_requirement=None):
        self.adv_name = adv_name
        self.adv_reward = adv_reward
        self.adv_requirement = adv_requirement

    def __repr__(self):
        return f'{self.adv_name}, {self.adv_reward}, {self.adv_requirement}'

