from modules.ascii_art import dagger_art, katana_art, claimore_art, axe_art, sword_art


class GameFlowBool:
    """
    Class that holds boolean logic to control flow of the game
    """
    def __init__(self, fight, hero_created, alive, key, treasure_chest, sewers, dessert, loaded_game, first_attack):
        self.fight = fight
        self.hero_created = hero_created
        self.alive = alive
        self.key = key
        self.treasure_chest = treasure_chest
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

    def enemy_zone_menu(self):
        """
        Displays navigation options depending on a current position of the map
        Hides corresponding options if player is next to the edge of the map
        """
        if self.x > 0:
            print(  # Selects location name based on coordinates and paces text in fixed position
                ' ' * 8, f'1. Go North to {self.enemy_zone[self.x-1][self.y]}',
                ' ' * (30 - len(f'{self.enemy_zone[self.x-1][self.y]}')),
                'Q. Open Menu')
        else:
            print(' ' * 55, 'Q. Open Menu')
        if self.y < len(self.enemy_zone[self.x]) - 1:
            print(  # Selects location name based on coordinates and paces text in fixed position
                ' ' * 8, f'2. Go East to {self.enemy_zone[self.x][self.y+1]}',
                ' ' * (31 - len(f'{self.enemy_zone[self.x][self.y+1]}')),
                'W. Character Info')
        else:
            print(' ' * 55, 'W. Character Info')
        if self.x < len(self.enemy_zone) - 1:
            print(  # Selects location name based on coordinates and paces text in fixed position
                ' ' * 8, f'3. Go South to {self.enemy_zone[self.x+1][self.y]}',
                ' ' * (30 - len(f'{self.enemy_zone[self.x+1][self.y]}')),
                'E. Open stash')
        else:
            print(' ' * 55, 'E. Open stash')
        if self.y > 0:
            print(' ' * 8, f'4. Go West to {self.enemy_zone[self.x][self.y-1]}')


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

    def stats(self):
        """
        Character stats
        """
        print('\n')
        print('   ≥φäðœ‰~-                                                          -~‰œðäφ≥   ')
        print('   ‘æ%  ╔══                                                          ══╗  %æ‘   ')
        print('     δ  ║           Health:', ' ' * 20, f'{self.max_health}', ' ' * (20 - len(str(self.max_health))), '║  δ')
        print('     :              Attack:', ' ' * 20, f'{self.attack}', ' ' * (20 - len(str(self.attack))), '   :')
        print('     :              Potions:', ' ' * 19, f'{self.health_potion}', ' ' * (20 - len(str(self.health_potion))), '   :')
        print('     δ  ║           Gold:', ' ' * 22, f'{self.gold}', ' ' * (20 - len(str(self.gold))), '║  δ')
        print('   ‘æ%  ╚══                                                          ══╝  %æ‘   ')
        print('  ‘≥φäðœ‰~-                                                          -~‰œðäφ≥‘  \n')
        print('W. Go Back\n')


class Enemy(Character):
    """
    Encounterable enemies subclass
    """
    def __init__(self, *stats):
        super().__init__(*stats)
        self.spawn_area = stats[4]


class Items:
    """
    Game items
    """
    def __init__(self, *weapons):
        self.dagger = weapons[0]
        self.sword = weapons[1]
        self.mace = weapons[2]
        self.flail = weapons[3]
        self.hammer = weapons[4]

    def weapon_art(self, weapon):
        if weapon[0] == 'Dagger':
            dagger_art()
        if weapon[0] == 'Katana':
            katana_art()
        if weapon[0] == 'Claimore':
            claimore_art()
        if weapon[0] == 'Axe':
            axe_art()
        if weapon[0] == 'Sword':
            sword_art()
            