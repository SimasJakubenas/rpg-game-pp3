class Game_flow_bool:
    """
    Class that holds boolean logic to control flow of the game
    """
    def __init__(self, fight, hero_created, alive, key, store_health_pots, treasure_chest, replace, sewers, dessert, loaded_game):
        self.fight = fight
        self.hero_created = hero_created
        self.alive = alive
        self.key = key
        self.store_health_pots = store_health_pots
        self.treasure_chest = treasure_chest
        self.replace = replace
        self.sewers = sewers
        self.dessert = dessert
        self.loaded_game = loaded_game

class Location:
    """
    Hold variable that are used to control movement
    """
    def __init__(self, current_location, enemy_zone, x, y):
        self.current_location = current_location
        self.enemy_zone = enemy_zone
        self.x = x
        self.y = y

class Character:
    """
    Superclass for all playeable characters and enemies in the game
    """
    # properties
    def __init__(self, *stats):
        self.name = stats[0]
        self.health = stats[1]
        self.max_health = int(stats[1])
        self.attack = int(stats[2])
        self.gold = int(stats[3])

class Hero(Character):
    """
    Playable characters subclass
    """
    def __init__(self, *stats):
        super().__init__(*stats)
        self.health_potion = int(stats[4])

class Enemy(Character):
    """
    Encounterable enemies subclass
    """
    def __init__(self, *stats):
        super().__init__(*stats)
        self.spawn_area = stats[4]
