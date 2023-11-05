import gspread
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
    
    fight = False
    menu = False

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
    navigate_town = input()
    while True:
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

    x = 2
    y = 2
    while True:
        print(f'You have entered {sewers_zone[x][y]}')

        # If statements hide the movement options if you've reached corresponding edge of map
        if x > 0:
            print(f'1. Go North to {sewers_zone[x-1][y]}')
        if y < len(sewers_zone[x]) - 1:
            print(f'2. Go East to {sewers_zone[x][y+1]}')
        if x < len(sewers_zone) - 1:
            print(f'3. Go South to {sewers_zone[x+1][y]}')
        if y > 0:
            print(f'4. Go West to {sewers_zone[x][y-1]}')

        sewers_controls = input()
        # 'And' operators prevents game from crashing if player tries to move out of map
        if sewers_controls == '1' and x > 0:
            x -= 1
        if sewers_controls == '2' and y < len(sewers_zone[x]) - 1:
            y += 1
        if sewers_controls == '3' and x < len(sewers_zone) -1 :
            x += 1
        if sewers_controls == '4' and y > 0:
            y -= 1

def battle(current_loc, char_list, hero_stats):
    global current_health, alive, fight
    enemy_list = slice(2, 5)
    while fight:
        enemy = tuple(random.choice(char_list[enemy_list]))

        if enemy[4] == current_loc:
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
                gen = True
                input()
                main()
            print('Your Life')
            print(f'{current_health}/{int(hero_stats.health)}')
            print(f'{enemy_stats.name} Life')
            print(f'{current_enemy_health}/{int(enemy_stats.health)}')
            print('1. Attack')
            print('2. Use Potion')
            battle_option = input()

            if battle_option == '1':
                current_enemy_health -= hero_dmg
                print(f'You have done {hero_dmg} damage to {enemy_stats.name}')
                if current_enemy_health <= 0:
                    print(f'{enemy_stats.name} has fallen')
                    gen = True
                    return current_health

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