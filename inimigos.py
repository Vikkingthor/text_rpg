from personagem import Character
import random

class Enemy(Character):
    def __init__ (self, name, life, defense, strength, experience, level):
        super().__init__(name, life, defense, strength, experience, level)

    def Enemy_attack (self, target):
        dmg = random.randint(0, self.strength)
        if dmg == 0:
            dmg = 0
        target.life -= dmg
        print(f"{self.name} causou {dmg} pontos de dano em {target}")
        return target.life
    
    def is_alive (self):
        return self.life > 0


def lv1_enemies():
    enemy1 = Enemy(name = "Ratazana", life = 10, defense = 5, strength = 5, experience = 10, level = 1)
    enemy2 = Enemy(name = "Viper", life = 10, defense= 5, strength = 6, experience = 10, level = 1)
    enemy3 = Enemy(name = "Slime", life = 15, defense = 3, strength= 3, experience= 10, level= 2)
    enemy4 = Enemy (name = "Tombstone", life = 25, defense = 8, strength = 7, experience = 40, level = 5)

    return [enemy1, enemy2, enemy3, enemy4]

def random_enemy(enemies):
    return random.choice(enemies)