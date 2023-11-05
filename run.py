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
    
    global fight, menu, alive, key

    fight = False
    menu = False
    alive = True
    key = False

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
            pass
        else:
            print('Select Menu Option by entering a number 1-5')

def town_zone():
    """
    Starting game zone with that prompts the player to navigate the game
    """
    global current_health

    char_list = SHEET.worksheet('chars').get_all_values()
    hero = tuple(char_list[1])
    hero_stats = Hero(*hero)
    current_health = int(hero_stats.health)
    health_potion = int(hero_stats.health_pot)

    print('Welcome to the town of Lut Gholein! What would you like to do?')
    print('1. Go to Sewers')
    while True:
        navigate_town = input()
        if navigate_town == '1':
            sewers_zone_navigation(char_list, hero_stats, health_potion)
        elif navigate_town == '2':
            pass
        elif navigate_town == '3':
            pass
        elif navigate_town == '4':
            pass
        else:
            print('Enter a number 1-4 to select your destination')

def sewers_zone_navigation(char_list, hero_stats, health_potion):
    """
    Pulls sewers map from the spreadsheet and defines movement
    """
    sewers_zone = SHEET.worksheet('sewers').get_all_values()
    # Variables that check if player is trying to go outside of the map
    global fight

    x = 2
    y = 2

    while True:
        off_north_wall = x > 0
        off_east_wall = y < len(sewers_zone[x]) - 1
        off_south_wall = x < len(sewers_zone) - 1
        off_west_wall = y > 0
        current_loc = sewers_zone[x][y]

        print(f'You have entered {current_loc}')
        print(f'You have {health_potion} hp pots')
        if current_loc != 'Dungeon Gate':
            if fight:
                battle(current_loc, char_list, hero_stats, health_potion)
                health_potion += 1
                fight = False
        # If statements hide the movement options if you've reached corresponding edge of map
        if off_north_wall:
            print(f'1. Go North to {sewers_zone[x-1][y]}')
        if off_east_wall:
            print(f'2. Go East to {sewers_zone[x][y+1]}')
        if off_south_wall:
            print(f'3. Go South to {sewers_zone[x+1][y]}')
        if off_west_wall:
            print(f'4. Go West to {sewers_zone[x][y-1]}')

        sewers_controls = input()
        # 'And' operators prevents game from crashing if player tries to move out of map
        if sewers_controls == '1' and off_north_wall:
            x -= 1
            fight = True
        if sewers_controls == '2' and off_east_wall:
            y += 1
            fight = True
        if sewers_controls == '3' and off_south_wall:
            x += 1
            fight = True
        if sewers_controls == '4' and off_west_wall:
            y -= 1
            fight = True

def battle(current_loc, char_list, hero_stats, health_potion):
    global current_health, current_enemy_health, alive, fight, key
    enemy_list = slice(2, 6)
    while fight:
        enemy = tuple(random.choice(char_list[enemy_list]))

        if enemy[4] == current_loc:
            if enemy[0] == 'Radement' and key == True:
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

            battle_options(enemy, hero_dmg, hero_stats, enemy_stats, health_potion)

def battle_options(enemy, hero_dmg, hero_stats, enemy_stats, health_potion):
    """
    Takes user input of a battle option and runs corresponding action
    """
    global current_enemy_health, current_health, key

    while True:
        battle_option = input()
        # Option to attack
        if battle_option == '1':
            current_enemy_health -= 50
            print(f'You have done {hero_dmg} damage to {enemy_stats.name}')
            if current_enemy_health <= 0:
                print(f'{enemy_stats.name} has fallen')
                if enemy[0] == 'Radement':
                    key = True
                    print('Would you like to return to town?')
                    while True:
                        town_portal = input('Y/N: ')
                        if town_portal.lower() == 'y':
                            town_zone()
                        elif town_portal.lower() == 'n':
                            return False
                        else:
                            print('Type in "y" to go back to town or "N" to stay')
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