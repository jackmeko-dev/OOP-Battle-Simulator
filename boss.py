import random
from enemy import Enemy

class Boss(Enemy):
    def __init__(self, name):
        self.name = name
        self.health = 250
        self.attack_power = random.randint(50, 70)

    def attack(self):
        return random.randint(10, self.attack_power)
    def specialattack(self):
        if self.attack_power <=30:
            self.attack_power = 100
            print("FIRE BLAST!!!!")
