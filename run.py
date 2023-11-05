import gspread, random
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Tal-Rasha')

def main():
    """
    Main game function
    """
    
    global fight, menu, alive, key, store_health_pots, treasure_chest

    fight = False
    menu = False
    alive = True
    key = False
    store_health_pots = False
    treasure_chest = True

    title_and_greeting()

def title_and_greeting():
    """
    Adds title art and greeting to the players letting them know what kind of game this is

    """
    print('                                                                              ')
    print('  ▄▄▄█████▓ ▄▄▄       ██▓        ██▀███   ▄▄▄        ██████  ██░ ██  ▄▄▄      ')
    print('  ▓  ██▒ ▓▒▒████▄    ▓██▒       ▓██ ▒ ██▒▒████▄    ▒██    ▒ ▓██░ ██▒▒████▄    ')
    print('  ▒ ▓██░ ▒░▒██  ▀█▄  ▒██░       ▓██ ░▄█ ▒▒██  ▀█▄  ░ ▓██▄   ▒██▀▀██░▒██  ▀█▄  ')
    print('  ░ ▓██▓ ░ ░██▄▄▄▄██ ▒██░       ▒██▀▀█▄  ░██▄▄▄▄██   ▒   ██▒░▓█ ░██ ░██▄▄▄▄██ ')
    print('    ▒██▒ ░  ▓█   ▓██▒░██████▒   ░██▓ ▒██▒ ▓█   ▓██▒▒██████▒▒░▓█▒░██▓ ▓█   ▓██▒')
    print('    ▒ ░░    ▒▒   ▓▒█░░ ▒░▓  ░   ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒ ▒▒   ▓▒█░')
    print('      ░      ▒   ▒▒ ░░ ░ ▒  ░     ░▒ ░ ▒░  ▒   ▒▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░  ▒   ▒▒ ░')
    print('    ░        ░   ▒     ░ ░        ░░   ░   ░   ▒   ░  ░  ░   ░  ░░ ░  ░   ▒   ')
    print('                 ░  ░    ░  ░      ░           ░  ░      ░   ░  ░  ░      ░  ░')
    print('                                                                              ')
    print('                    Welcome to a Diablo II themed RPG game                    ')
    input('                             Press ENTER to play ')
    game_menu_display()

def game_menu_display():
    """
    Calls for game menu and requires user input to select menu item
    """
    print('\n')
    print('                       <++xxxwwwwwwwwwwWWWWWWwwxxx++>')
    print('                       ░                            ░')
    print('                       ░          GAME MENU         ░')
    print('                       ░        1. New Game         ░')
    print('                       ░        2. Save Game        ░')
    print('                       ░        3. Load Game        ░')
    print('                       ░        4. Rules            ░')
    print('                       ░        5. End game         ░')
    print('                       ░                            ░')
    print('                       <++xxxwwWWWWWWWwwwwwwwwwxxx++>')
    
    game_menu_select()

def game_menu_select():
    """
    Selects menu option baed of user input
    """
    while True:
        menu_item = input()
        if menu_item == '1':
            town_zone()
            return False
        elif menu_item == '2':
            pass
        elif menu_item == '3':
            pass
        elif menu_item == '4':
            pass
        elif menu_item == '5':
            quit()
        else:
            print('Select Menu Option by entering a number 1-5')

def town_zone():
    """
    Starting game zone with that prompts the player to navigate the game
    """
    global current_health, health_potion, store_health_pots, sewers, dessert

    char_list = SHEET.worksheet('chars').get_all_values()
    hero = tuple(char_list[1])
    hero_stats = Hero(*hero)
    current_health = int(hero_stats.health)
    sewers = False
    dessert = False
    if store_health_pots == False:
        health_potion = int(hero_stats.health_pot)
        store_health_pots = True

    print('Welcome to the town of Lut Gholein! What would you like to do?')
    
    while True:
        print('1. Go to Sewers')
        print('2. Go to Dessert')
        navigate_town = input()
        if navigate_town == '1':
            sewers = True
            enemy_zone_navigation(char_list, hero_stats)
        elif navigate_town == '2':
            if key == True:
                dessert = True
                enemy_zone_navigation(char_list, hero_stats)
            else:
                print('Town Gate is locked!')
        elif navigate_town == '3':
            pass
        elif navigate_town == '4':
            pass
        else:
            print('Enter a number 1-4 to select your destination')

def enemy_zone_navigation(char_list, hero_stats):
    """
    Pulls sewers map from the spreadsheet and defines movement
    """
    global health_potion, fight, treasure_chest, sewers, dessert

    if sewers == True:
        enemy_zone = SHEET.worksheet('sewers').get_all_values()
        x = 2
        y = 2
    if dessert == True:
        enemy_zone = SHEET.worksheet('dessert').get_all_values()
        x = 1
        y = 1
    
    while True:
        # Variables that check if player is trying to go outside of the map
        off_north_wall = x > 0
        off_east_wall = y < len(enemy_zone[x]) - 1
        off_south_wall = x < len(enemy_zone) - 1
        off_west_wall = y > 0
        current_loc = enemy_zone[x][y]

        print(f'You have entered {current_loc}')
        print(f'You have {health_potion} hp pots')
        if current_loc != 'Dungeon Gate' or 'Town Gate':
            if current_loc == 'Sewers Hideout':
                if treasure_chest == True:
                    print('You found 200 gold!')
                    treasure_chest = False
                    fight = False
                else:
                    battle(current_loc, char_list, hero_stats)
            if fight:
                battle(current_loc, char_list, hero_stats)
                health_potion += 1
                fight = False
        else:
            if fight:
                fight = False
                return_to_town()
        # If statements hide the movement options if you've reached corresponding edge of map
        if off_north_wall:
            print(f'1. Go North to {enemy_zone[x-1][y]}')
        if off_east_wall:
            print(f'2. Go East to {enemy_zone[x][y+1]}')
        if off_south_wall:
            print(f'3. Go South to {enemy_zone[x+1][y]}')
        if off_west_wall:
            print(f'4. Go West to {enemy_zone[x][y-1]}')

        zone_controls = input()
        # 'And' operators prevents game from crashing if player tries to move out of map
        if zone_controls == '1' and off_north_wall:
            x -= 1
            fight = True
        if zone_controls == '2' and off_east_wall:
            y += 1
            fight = True
        if zone_controls == '3' and off_south_wall:
            x += 1
            fight = True
        if zone_controls == '4' and off_west_wall:
            y -= 1
            fight = True

def battle(current_loc, char_list, hero_stats):
    """
    Battle function determines an enemy encounter depending on map area
    Loops through a fight until either player or enemy dies
    Provide player with battle options
    """
    global current_health, current_enemy_health, health_potion, alive, fight, key
    if sewers == True:
        enemy_list = slice(2, 7)
    if dessert == True:
        enemy_list = slice(7, 19)
    while fight:
        enemy = tuple(random.choice(char_list[enemy_list]))
            
        if enemy[4] == current_loc:
            if (enemy[0] == 'Radement' and key == True) \
                or (current_loc == 'Sewers Hideout' and treasure_chest == False):
                enemy_list = slice(2, 5)
                enemy = tuple(random.choice(char_list[enemy_list]))
            enemy_stats = Enemy(*enemy)
            print(f'You have been attacked by {enemy[0]}')
            mob_dmg = int(enemy_stats.attack)
            hero_dmg = int(hero_stats.attack)
            current_enemy_health = int(enemy_stats.health)
            fight = False
        
    if alive:
        while current_enemy_health > 0:
            print(f'{enemy_stats.name} has done {enemy_stats.attack} damage to you')
            current_health -= mob_dmg

            if current_health <= 0:
                print('GAME OVER')
                alive = False
                input()
                main()
            print('Your Life')
            print(f'{current_health}/{int(hero_stats.health)}')
            print(f'{enemy_stats.name} Life')
            print(f'{current_enemy_health}/{int(enemy_stats.health)}')
            print('1. Attack')
            print('2. Use Potion')

            battle_options(enemy, hero_dmg, hero_stats, enemy_stats)

def battle_options(enemy, hero_dmg, hero_stats, enemy_stats):
    """
    Takes user input of a battle option and runs corresponding action
    """
    global current_enemy_health, current_health, health_potion, key

    while True:
        battle_option = input()
        # Option to attack
        if battle_option == '1':
            current_enemy_health -= hero_dmg
            print(f'You have done {hero_dmg} damage to {enemy_stats.name}')
            if current_enemy_health <= 0:
                print(f'{enemy_stats.name} has fallen')
                if enemy[0] == 'Radement':
                    key = True

                    return_to_town()
                
            return current_enemy_health
        # Option to heal
        elif battle_option == '2':
            if health_potion > 0:
                current_health += 50
                if current_health > int(hero_stats.max_health):
                    current_health = int(hero_stats.max_health)
                health_potion -= 1
                return current_health
            else:
                print('You have no health pots')
            return False
        else:
            print('Type a number 1-n to select battle option')

def return_to_town():
    print('Would you like to return to town?')
    while True:
        town_portal = input('Y/N: ')
        if town_portal.lower() == 'y':
            town_zone()
            
        elif town_portal.lower() == 'n':
            return False
        else:
            print('Type in "y" to go back to town or "N" to stay')

# Classes
class Character():
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

main()