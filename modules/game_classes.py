class Game_flow_bool:
    """
    Class that holds boolean logic to control flow of the game
    """
    def __init__(self, fight, hero_created, alive, key, treasure_chest, replace, sewers, dessert, loaded_game, first_attack):
        self.fight = fight
        self.hero_created = hero_created
        self.alive = alive
        self.key = key
        self.treasure_chest = treasure_chest
        self.replace = replace
        self.sewers = sewers
        self.dessert = dessert
        self.loaded_game = loaded_game
        self.first_attack = first_attack

class Worksheets:
    """
    Class that hold all the worksheets used in the game
    """
    def __init__(self, sewers_map, dessert_map, characters, items, shop, stash, save, stash_save):
        self.sewers_map = sewers_map
        self.dessert_map = dessert_map
        self.characters = characters
        self.items = items
        self.vendor = shop
        self.stash = stash
        self.save = save
        self.stash_save = stash_save

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
        self.health = int(stats[1])
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
