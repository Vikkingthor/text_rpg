#Character irá valer para os inimigos também, porém se strength, xl e lv.
class Character:
    def __init__ (self, name, life, defense, strength, experience, level):
        self.name = name
        self.life = life
        self.defense = defense
        self.strength = strength
        self.experience = experience
        self.level = level

    def __str__(self):
        return f"Name: {self.name}\n Life: {self.life}\n Defense: {self.defense}\n Str: {self.strength}\n Level: {self.level}\n Battle XP: {self.experience}"
#Ataque do personagem, também será herdado para os inimigos    
    def attack (self, target):
        dmg = self.strength - target.defense
        if self.strength < 0:
            dmg = 0
            print(f"Você causou {dmg} pontos de dano. {target.name}:{target.life}")
        target.life -= dmg
        return dmg
    #Verifica se ainda tem hp
    def is_alive (self):
        return self.life > 0

#Analisa se a entrada do usuário é válida
def check_name (name):
    if not name.isalpha() or name == str :
        print('Hm... Não. Tenta de novo.')
        return False
    return True