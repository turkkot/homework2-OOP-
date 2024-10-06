class Person:
    def __init__(self, health, damage, armor):
        self.health = health
        self.damage = damage
        self.armor = armor

    def calculate_damage(self, damage):
        return damage * (1 - self.armor / 100)

    def take_damage(self, damage):
        damage_taken = self.calculate_damage(damage)
        self.health -= damage_taken
        armor_reduction = damage * 0.2
        self.armor -= armor_reduction

        if self.armor < 0:
            self.armor = 0
        if self.health < 0:
            self.health = 0

    def print_stat(self, entity_name):
        print(f'{entity_name} has {self.health:.1f} hp and {self.armor:.1f} armor strength')

    def attack(self, target):
        target.take_damage(self.damage)


class Player(Person):
    def __init__(self, health, damage, armor, name):
        super().__init__(health, damage, armor)
        self.name = name

    def attack_enemy(self, target):
        print(f'{self.name} attacks {target.enemy_type} and deals {self.damage} damage')
        self.attack(target)
        target.print_stat(target.enemy_type)


class Enemy(Person):
    def __init__(self, health, damage, armor, enemy_type):
        super().__init__(health, damage, armor)
        self.enemy_type = enemy_type

    def attack_player(self, player):
        print(f'{self.enemy_type} attacks {player.name} and deals {self.damage} damage')
        self.attack(player)
        player.print_stat(player.name)


evilKnight = Enemy(50, 20, 50, "Evil Knight")
player = Player(100, 20, 100, "Player1")


while player.health > 0 and evilKnight.health > 0:
    player.attack_enemy(evilKnight)
    if evilKnight.health <= 0:
        print(f'{evilKnight.enemy_type} is dead!')
        break

    evilKnight.attack_player(player)
    if player.health <= 0:
        print(f'{player.name} is dead!')
        break