import pygame

class Weapon:

    def __init__(self, weapon_name, damage, requirement=None):
            self.weapon_name = weapon_name
            self.damage = damage
            self.requirement = requirement

    def getWeaponName(self):
            return self.weapon_name

    def getWeaponDamage(self):
            return self.damage

    def getWeaponRequirement(self):
            return self.requirement

class Fist (Weapon):

    def __init__(self):
        super().__init__("Fist", 5, None)

class WoodenSword (Weapon):

    def __init__(self):
        super().__init__("Wooden Sword", 7, None)


