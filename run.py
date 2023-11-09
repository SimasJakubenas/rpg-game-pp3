import gspread, random, os
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
    
    global fight, hero_created, alive, key, store_health_pots, treasure_chest

    fight = False
    hero_created = False
    alive = False
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
    input('                             Press ENTER to play\n')
    clear()
    game_menu_display()
    game_menu_select()

def game_menu_display():
    """
    Calls for game menu and requires user input to select menu item
    ASCII art was created with https://www.asciiart.eu/image-to-ascii
    """

    print('\n')
    print('                               ...:*@@@@@@@@@*:..      ')
    print('                             .*@@=..   =@. ..=@@*..    ')
    print('                          ..#@+.      .@@%.    .+@%..  ')
    print('                         .-@+.,-----------------,.+@=. ')
    print('                        .-@:  |    GAME MENU    |  .@+.')
    print('                        -@+@@@|                 |...:@-')
    if hero_created == False:
        print('                        #%..:@|   1. New Game   |@@@+%%')
    else:
        print('                        #%..:@|   1. Continue   |@@@+%%')
    print('                        @*   .|   2. Save Game  |+.  +@')
    print('                        @*    |   3. Load Game  |    +@')
    print('                        *%    |   4. Rules      |   .%#')
    print('                        :@:.  |   5. End game   |  .:@-')
    print('                        .-@:  "-----------------" .:@=.')
    print('                         .:@+..@@@+.     .:@@@*. .+@-. ')
    print('                           .*@%=.           .*@.+@#..  ')
    print('                             .+@@=....   ....=@@*.     ')
    print('                               ..-*@@@@@@@@@*-..       ')

def game_menu_select():
    """
    Selects menu option based of user input
    """
    global hero_created, alive

    while True:
        menu_item = input('\n')
        clear()
        game_menu_display()
        if menu_item == '1':
            menu_item = 'start'
            if alive == False:
                if hero_created == False:
                    menu_option(menu_item)
                else:
                    town_zone()
            else:
                clear()
                location_art()
                if current_loc == 'Lut Gholein':
                    ingame_menu()
                else:
                    zone_navigation_menu(enemy_zone, x, y)
                return False
        # Game save
        elif menu_item == '2':
            if alive == False:
                menu_item = 'start'
                print('Start the game first')
                menu_option(menu_item)
            else:
                menu_item = 'save'
                menu_option(menu_item)
        # Game load
        elif menu_item == '3':
            menu_item = 'load'
            menu_option(menu_item)
            
        elif menu_item == '4':
            pass
        # Game quit
        elif menu_item == '5':
            menu_item = 'quit'
            menu_option(menu_item)
        else:
            print('')
            print('Select Menu Option by entering a number 1-5')

def menu_option(menu_item):
    """
    Calls appropriate functions that corresponds with players input 
    """
    global alive, hero_created

    print('')
    while True:
        want_to_quit = input(f"Do you want to {menu_item} the game?Y/N\n")
        clear()

        if want_to_quit.lower() == 'y':
            if menu_item == 'start':
                alive = True
                hero_created = True
                hero_selection()
                town_zone()
            if menu_item == 'save':
                save_game()
                game_menu_display()
                print('The game was saved...')
            if menu_item == 'load':
                print('The game was loaded...')
                hero_selection()
                load_game()
                town_zone()
            if menu_item == 'quit':
                quit()
        elif want_to_quit.lower() == 'n':
            game_menu_display()
            return False
        else:
            game_menu_display()
            print('')
            print('Type in "y" to save or "N" to go back to menu')

def save_game():
    """
    Saves the game by pushing hero stats to a google spreadsheet
    """
    global hero, hero_gold, health_potion

    hero_stats_pull = Hero(hero[0], hero[1], hero[2], hero_gold, health_potion)
    hero_stats_dict = vars(hero_stats_pull)
    hero_stats_list = list(hero_stats_dict.values())
    save_file = SHEET.worksheet('save')
    save_file.append_row(hero_stats_list)
    print(hero_stats_list)

def load_game():
    """
    Loads the game by pulling character stats from save worksheet
    """
    global hero_stats, hero_gold, health_potion, hero

    load_list = SHEET.worksheet('save').get_all_values()
    last_save = load_list[-1]
    hero_gold = int(last_save[4])
    health_potion = int(last_save[5])
    hero_stats = Hero(hero[0], hero[1], hero[2], hero_gold, health_potion)

def hero_selection():
    """
    Creates hero character by pulling values from a spreadsheet
    """
    global hero_gold, hero_stats, char_list, hero

    char_list = SHEET.worksheet('chars').get_all_values()
    hero = tuple(char_list[1])
    hero_stats = Hero(*hero)
    hero_gold = int(hero_stats.gold)

def town_zone():
    """
    Starting game zone with that prompts the player to navigate the game
    """
    global current_health, health_potion, store_health_pots, hero_stats, char_list, sewers, dessert, current_loc

    current_loc = 'Lut Gholein'
    current_health = int(hero_stats.health)
    sewers = False
    dessert = False
    if store_health_pots == False:
        health_potion = int(hero_stats.health_pot)
        store_health_pots = True
    location_art()
    ingame_menu()
    while True:
        navigate_town = input('\n')
        clear()
        if navigate_town == '1':
            sewers = True
            enemy_zone_navigation(char_list, hero_stats)
        elif navigate_town == '2':
            if key == True:
                dessert = True
                enemy_zone_navigation(char_list, hero_stats)
            else:
                location_art()
                ingame_menu()
                print('Town Gate is locked!')
        elif navigate_town == '3':
            pass
        elif navigate_town.lower() == 'q':
            game_menu_display()
            game_menu_select()
        else:
            location_art()
            ingame_menu()
            print('Enter a number 1-4 to select your destination')

def enemy_zone_navigation(char_list, hero_stats):
    """
    Pulls sewers map from the spreadsheet and defines movement
    """
    global health_potion, fight, treasure_chest, hero_gold, sewers, dessert, current_loc, x, y, enemy_zone

    if sewers == True:
        enemy_zone = SHEET.worksheet('sewers').get_all_values()
        x = 2
        y = 2
    if dessert == True:
        enemy_zone = SHEET.worksheet('dessert').get_all_values()
        x = 1
        y = 1
    current_loc = enemy_zone[x][y]
    location_art()
    zone_navigation_menu(enemy_zone, x, y)
    while True:
        text_fix = False
        
        current_loc = enemy_zone[x][y]
        if (current_loc != 'Dungeon Gate') and (current_loc != 'Town Gate'):
            if current_loc == 'Sewers Hideout':
                if treasure_chest == True:
                    location_art()
                    print('You found 200 gold!')
                    hero_gold += int(char_list[5][3])
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
                location_art()
                return_to_town()
        zone_controls = input('\n')
        clear()
        # 'And' operators prevents game from crashing if player tries to move out of map
        if zone_controls == '1' and x > 0:
            x -= 1
            fight = True
        elif zone_controls == '2' and y < len(enemy_zone[x]) - 1:
            y += 1
            fight = True
        elif zone_controls == '3' and x < len(enemy_zone) - 1:
            x += 1
            fight = True
        elif zone_controls == '4' and y > 0:
            y -= 1
            fight = True
        elif zone_controls.lower() == 'q':
            game_menu_display()
            game_menu_select()
        else:
            location_art()
            zone_navigation_menu(enemy_zone, x, y)
            print('')
            print('Use numers 1-4 to navigate the map')

def zone_navigation_menu(enemy_zone, x, y):
    """
    Displays navigation options depending on a current position of the map
    Hides corresponding options if player is next to the edge of the map
    """
    if x > 0:
        print(f'1. Go North to {enemy_zone[x-1][y]}')
    if y < len(enemy_zone[x]) - 1:
        print(f'2. Go East to {enemy_zone[x][y+1]}')
    if x < len(enemy_zone) - 1:
        print(f'3. Go South to {enemy_zone[x+1][y]}')
    if y > 0:
        print(f'4. Go West to {enemy_zone[x][y-1]}')
    print('')
    print('Q. Open Menu')

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
    location_art()
    while fight:
        enemy = tuple(random.choice(char_list[enemy_list]))
            
        if enemy[4] == current_loc:
            if (enemy[0] == 'Radement' and key == True) \
                or (current_loc == 'Sewers Hideout' and treasure_chest == False):
                enemy_list = slice(2, 5)
                enemy = tuple(random.choice(char_list[enemy_list]))
            enemy_stats = Enemy(*enemy)
            mob_dmg = int(enemy_stats.attack)
            hero_dmg = int(hero_stats.attack)
            current_enemy_health = int(enemy_stats.health)
            fight = False
    print(f'You have been attacked by {enemy[0]}')
    while current_enemy_health > 0:
        print(f'{enemy_stats.name} has done {enemy_stats.attack} damage to you')
        current_health -= mob_dmg

        if current_health <= 0:
            print('GAME OVER')
            alive = False
            input('\n')
            clear()
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
    global current_enemy_health, current_health, health_potion, hero_gold ,key

    while True:
        battle_option = input('\n')
        clear()
        location_art() 
        # Option to attack
        if battle_option == '1':
            current_enemy_health -= hero_dmg
            print(f'You have done {hero_dmg} damage to {enemy_stats.name}')
            if current_enemy_health <= 0:
                print(f'{enemy_stats.name} has fallen and dropped {enemy[3]} gold')
                print('')
                zone_navigation_menu(enemy_zone, x, y)
                hero_gold += int(enemy[3])
                print('')
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
        town_portal = input('Y/N:\n')
        clear()
        if town_portal.lower() == 'y':
            town_zone()
            
        elif town_portal.lower() == 'n':
            location_art()
            return False
        else:
            print('Type in "y" to go back to town or "N" to stay')

def clear():
    """
    Clears the screen on user input
    Taken from https://stackoverflow.com/questions/2084508/clear-terminal-in-python answer by 'poke'
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def location_art():
    """
    ASCII art to improve game looks
    """
    
    print('-.;:~■-■---' + '~' * len(current_loc) + '---■-■~:;.-')
    print(f'      >>►► {current_loc} ◄◄<<     ')
    print('-.;:~■-■---' + '~' * len(current_loc) + '---■-■~:;.-')
    print('')

def ingame_menu():
    """
    In game menu selection
    """
    print('1. Go to Sewers')
    print('2. Go to Dessert')
    print('')
    print('Q. Open Menu')
    print('')

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