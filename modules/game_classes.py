# Class that hold boolean logic to control flow of the game
class Game_flow_bool:
  def __init__(self, fight, hero_created, alive, key, store_health_pots, treasure_chest, replace, sewers, dessert):
    self.fight = fight
    self.hero_created = hero_created
    self.alive = alive
    self.key = key
    self.store_health_pots = store_health_pots
    self.treasure_chest = treasure_chest
    self.replace = replace
    self.sewers = sewers
    self.dessert = dessert

class Character:
    """
    Superclass for all playeable characters and enemies in the game
    """
    # properties
    def __init__(self, *stats):
        self.name = stats[0]
        self.health = stats[1]
        self.max_health = stats[1]
        self.attack = stats[2]
        self.gold = stats[3]

class Hero(Character):
    """
    Playable characters subclass
    """
    def __init__(self, *stats):
        super().__init__(*stats)
        self.health_pot = stats[4]

class Enemy(Character):
    """
    Encounterable enemies subclass
    """
    def __init__(self, *stats):
        super().__init__(*stats)
        self.spawn_area = stats[4]
