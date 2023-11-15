import gspread, random, os
from google.oauth2.service_account import Credentials
from modules.game_classes import Character, Hero, Enemy, Game_flow_bool

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Tal-Rasha')

# Sets initial boolean values in the Game_flow_bool class
initial_state = Game_flow_bool(False, False, False, False, False, True, False)

def main():
    """
    Main game function
    """
    
    global key, store_health_pots, treasure_chest, replace

    key = False
    store_health_pots = False
    treasure_chest = True
    replace = False

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

def game_lore():
    """
    Lore of the game 
    """
    print('')
    print('     Been wondering in the dessert for weeks in search of Duriel...')
    print('       I Must be getting close I can feel his evil presence.')
    print('      The towers of town Lut Gholein appeared in the distance.')
    print('                I will spend the night here\n')
    input('                  Press ENTER to continue')
    clear()


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
    if initial_state.hero_created == False:
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
    while True:
        menu_item = input('\n')
        clear()
        game_menu_display()
        if menu_item == '1':
            menu_item = 'start'
            if initial_state.alive == False:
                if initial_state.hero_created == False:
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
            if initial_state.alive == False:
                menu_item = 'start'
                print('Start the game first')
                menu_option(menu_item)
            else:
                menu_item = 'save'
                menu_option(menu_item)
        # Game load
        elif menu_item == '3':
            menu_item = 'load'
            initial_state.hero_created = True
            menu_option(menu_item)
            
        elif menu_item == '4':
            game_rules()
            game_rules_back()
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
    global loaded_game

    stash = SHEET.worksheet('stash')
    loaded_game = False
    print('')
    while True:
        want_to_quit = input(f"Do you want to {menu_item} the game?Y/N\n")
        clear()

        if want_to_quit.lower() == 'y':
            if menu_item == 'start':
                initial_state.alive = True
                initial_state.hero_created = True
                hero_selection()
                game_lore()
                SHEET.values_clear("stash!A2:F10000")
                # A space holder for equipped weapon
                stash.append_row(['Stick', '0', '0', '0', '5', '0'])
                town_zone()
            if menu_item == 'save':
                save_game()
                clear()
                game_menu_display()
                print('')
                print('The game was saved...')
                return False
            if menu_item == 'load':
                initial_state.alive = True
                loaded_game = True
                hero_selection()
                load_game()
                clear()
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
    Saves heros stats by pushing hero stats to a google spreadsheet
    Saves aquired items to a google spreadsheet
    """
    global hero, hero_gold, health_potion, hero_attack, hero_max_health

    print('Game saving please wait....')
    hero_stats_pull = Hero(hero[0], hero_max_health, hero_attack, hero_gold, health_potion)
    hero_stats_dict = vars(hero_stats_pull)
    hero_stats_list = list(hero_stats_dict.values())
    save_file = SHEET.worksheet('save')
    save_file.append_row(hero_stats_list)

    get_items = SHEET.worksheet('stash').get_all_values()
    save_items = SHEET.worksheet('stash_save')
    save_items.clear()
    for item in get_items:
        save_items.append_row(item)

def load_game():
    """
    Loads the game by pulling character stats from save worksheet
    Transfers save items to a relevant worksheet
    """
    global hero_stats, hero_gold, health_potion, hero, hero_max_health, hero_attack, current_health

    save_file = SHEET.worksheet('save').get_all_values()
    while True:
        if len(save_file) > 1:
            print('Game loading please wait....')
            last_save = save_file[-1]
            hero_gold = int(last_save[4])
            health_potion = int(last_save[5])
            hero_max_health = int(last_save[2])
            current_health = int(last_save[2])
            hero_attack = int(last_save[3])
            hero_stats = Hero(hero[0], hero_max_health, hero_attack, hero_gold, health_potion)

            load_items_list = SHEET.worksheet('stash_save').get_all_values()
            stash = SHEET.worksheet('stash')
            stash.clear()
            for item in load_items_list:
                stash.append_row(item)
            return False
        else:
            game_menu_display()
            print('You need to save the game first!')
            game_menu_select()


def game_rules():
    """
    Display game rules
    """
    clear()
    print('Welcome to the world of Tal Rasha traveler\n')
    print('Navigate the menu by pressing corresponding')
    print('number or letter and confirm it with "enter" key\n')
    print('Navigate the map by chosing any of the 4 directions. Once')
    print('you have reach the edge of map you will not be able to')
    print('advance further in that direction')
    print('Kill Duriel to complete the game\n')
    print('Talk to the Vendor he will be abe to help you to advance')
    print('to the new area\n')
    print('Best of luck traveler!\n')
    print('4. Back to menu\n')

def game_rules_back():
    """
    Game rules navigation
    """
    while True:
        back_to_menu = input('\n')
        if back_to_menu == '4':
            game_menu_display()
            game_menu_select()
        else:
            game_rules()
            print('Type "4" to go back to menu')

def hero_selection():
    """
    Creates hero character by pulling values from a spreadsheet
    """
    global hero_gold, hero_stats, char_list, hero, hero_max_health, hero_attack

    char_list = SHEET.worksheet('chars').get_all_values()
    hero = tuple(char_list[1])
    hero_stats = Hero(*hero)
    hero_gold = int(hero_stats.gold)
    hero_attack = int(hero_stats.attack)
    hero_max_health = int(hero_stats.max_health)

def town_zone():
    """
    Starting game zone with that prompts the player to navigate the game
    """
    global current_health, health_potion, store_health_pots, hero_stats, char_list, sewers, dessert, current_loc, loaded_game

    current_loc = 'Lut Gholein'
    current_health = int(hero_stats.health)
    sewers = False
    dessert = False
    if store_health_pots == False:
        health_potion = int(hero_stats.health_pot)
        store_health_pots = True
    location_art()
    ingame_menu()
    if loaded_game == True:
        print('The game was loaded...')
    loaded_game = False
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
        elif navigate_town.lower() == 'w':
            character_info()
        elif navigate_town.lower() == 'e':
            stash_open()
        elif navigate_town.lower() == 'r':
            vendor()
        else:
            location_art()
            ingame_menu()
            print('Enter a number 1-4 to select your destination')

def enemy_zone_navigation(char_list, hero_stats):
    """
    Pulls sewers map from the spreadsheet and defines movement
    """
    global health_potion, treasure_chest, hero_gold, sewers, dessert, current_loc, x, y, enemy_zone

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
        current_loc = enemy_zone[x][y]
        if (current_loc != 'Dungeon Gate') and (current_loc != 'Town Gate'):
            if current_loc == 'Sewers Hideout':
                if treasure_chest == True:
                    location_art()
                    zone_navigation_menu(enemy_zone, x, y)
                    print('')
                    print('You found 200 gold!')
                    hero_gold += int(char_list[5][3])
                    treasure_chest = False
                    initial_state.fight = False
                else:
                    # location_art()
                    battle(current_loc, char_list, hero_stats)
            if initial_state.fight:
                location_art()
                battle(current_loc, char_list, hero_stats)
                health_potion += 1
                initial_state.fight = False
        else:
            if initial_state.fight:
                initial_state.fight = False
                location_art()
                return_to_town()
        zone_controls = input('\n')
        clear()
        # 'And' operators prevents game from crashing if player tries to move out of map
        if zone_controls == '1' and x > 0:
            x -= 1
            initial_state.fight = True
        elif zone_controls == '2' and y < len(enemy_zone[x]) - 1:
            y += 1
            initial_state.fight = True
        elif zone_controls == '3' and x < len(enemy_zone) - 1:
            x += 1
            initial_state.fight = True
        elif zone_controls == '4' and y > 0:
            y -= 1
            initial_state.fight = True
        elif zone_controls.lower() == 'q':
            game_menu_display()
            game_menu_select()
        elif zone_controls.lower() == 'w':
            character_info()
        elif zone_controls.lower() == 'e':
            stash_open()
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
    global replace

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
    print('W. Character Info')
    print('E. Open stash')
    
    if replace == True:
        print(f'You left your loot behind')
    replace = False

def battle(current_loc, char_list, hero_stats):
    """
    Battle function determines an enemy encounter depending on map area
    Loops through a fight until either player or enemy dies
    Provide player with battle options
    """
    global current_health, current_enemy_health, health_potion key, first_attack

    first_attack = False
    if current_health > hero_max_health:
        current_health = hero_max_health
    if sewers == True:
        enemy_list = slice(2, 7)
    if dessert == True:
        enemy_list = slice(7, 19)
    while initial_state.fight: 
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
            initial_state.fight = False
            print(f'You have been attacked by {enemy[0]}')
    while current_enemy_health > 0:
        print(f'{enemy_stats.name} has done {enemy_stats.attack} damage to you')
        current_health -= mob_dmg

        if current_health <= 0:
            print('GAME OVER')
            initial_state.alive = False
            input('\n')
            clear()
            main()
        battle_menu(hero_stats, enemy_stats)

        battle_options(enemy, hero_dmg, hero_stats, enemy_stats)

def battle_menu(hero_stats, enemy_stats):
    """
    Display health of player and enemy and display menu options in battle
    """
    global current_enemy_health, current_health, hero_max_health

    print('Your Life')
    print(f'{current_health}/{hero_max_health}')
    print(f'{enemy_stats.name} Life')
    print(f'{current_enemy_health}/{int(enemy_stats.health)}')
    print('1. Attack')
    print('2. Use Potion')
    print('')

def battle_options(enemy, hero_dmg, hero_stats, enemy_stats):
    """
    Takes user input of a battle option and runs corresponding action
    """
    global current_enemy_health, current_health, health_potion, hero_gold , key, first_attack, hero_attack

    while True:
        battle_option = input('\n')
        clear()
        location_art() 
        # Option to attack
        if battle_option == '1':
            first_attack = True
            current_enemy_health -= hero_attack
            print(f'You have done {hero_attack} damage to {enemy_stats.name}')
            if current_enemy_health <= 0:
                print(f'{enemy_stats.name} has fallen and dropped {enemy[3]} gold')
                item_drop()
                print('')
                zone_navigation_menu(enemy_zone, x, y)
                hero_gold += int(enemy[3])
                print('')
                if enemy[0] == 'Radement':
                    key = True
                    clear()
                    location_art()
                    return_to_town()
                if enemy[0] == 'Duriel':
                    game_win_logo()
                    game_win()
                
            return current_enemy_health
        # Option to heal
        elif battle_option == '2':
            if health_potion > 0:
                current_health += 50
                if current_health > hero_max_health:
                    current_health = hero_max_health
                health_potion -= 1
                print('You gained 50 life!')
                return current_health
            else:
                battle_menu(hero_stats, enemy_stats)
                print('You have no health pots')
        else:
            if first_attack == False:
                print(f'You have been attacked by {enemy[0]}')
            else:
                print(f'You have done {hero_attack} damage to {enemy_stats.name}')
            print(f'{enemy_stats.name} has done {enemy_stats.attack} damage to you')
            battle_menu(hero_stats, enemy_stats)
            print('Type a number 1-n to select battle option')

def item_drop():
    """
    Chance to aquire item after a fight
    """
    global replace

    stash = SHEET.worksheet('stash')
    stash_list = SHEET.worksheet('stash').get_all_values()
    item_list = SHEET.worksheet('items').get_all_values()
    weapon_list = item_list[3:]
    for weapon in weapon_list:
        if float(weapon[-1]) >= random.random():
            print(f'You found {weapon[0]}\n')
            stash.append_row(weapon)
            stash_list.append(weapon)
        while len(stash_list) > 8:
            remove_item = input(f'Not enough space in stash would you like to remove {stash_list[1][0]}?Y/N\n')
            clear()
            if remove_item.lower() == 'y':
                remove_first = stash_list.pop(1)
                stash.clear()
                for row in stash_list:
                    stash.append_row(row)
                location_art()
            elif remove_item.lower() == 'n':
                del stash_list[-1]
                stash.clear()
                for row in stash_list:
                    stash.append_row(row)
                replace = True
                location_art()
            else:
                location_art()
                print(f'You found {weapon[0]}\n')
                print(f'Press "Y" to replace {stash_list[1][0]} or "N" to pass on this item')

def stash_open():
    """
    Display aquired items
    Pull and display relevant data from 'stash' spreadsheet
    """
    global hero_attack, hero_max_health, stash, stash_sheet

    location_art()
    stash_menu()
    while True:
        equip = input('\n')
        clear()
        location_art()
        if equip == '1' or equip == '2' or equip == '3' or equip == '4' or equip == '5' or equip == '6' or equip == '7':
            stash_sheet = SHEET.worksheet('stash').get_all_values()
            if 0 < int(equip) < len(stash_sheet):
                stash_menu()
                print(f'Would you like to equip {stash_sheet[int(equip)+1][0]}?')
                equip_confirm = input('Y/N\n')
                if equip_confirm.lower() == 'y':
                    stash_limit = stash_sheet[1:9]
                    equipped_weapon = stash_limit.pop(int(equip))
                    stash = SHEET.worksheet('stash')
                    SHEET.values_clear("stash!A2:F10000")
                    hero_attack = int(hero[2]) + int(equipped_weapon[1])
                    hero_max_health = int(hero[1]) + int(equipped_weapon[2])
                    stash.append_row(equipped_weapon)
                    for row in stash_limit:
                        stash.append_row(row)
                    stash = SHEET.worksheet('stash')
                    stash_sheet = SHEET.worksheet('stash').get_all_values()
                    clear()
                    location_art()
                    stash_menu()
                elif equip_confirm.lower() == 'n':
                    clear()
                    location_art()
                    stash_menu()
                else:
                    stash_menu()
                    print('Type "Y" to confirm to equip or "N" to cancel')
            else:
                print(f'Type number to equip item or "R" to go back')
        elif equip.lower() == 'e':
            clear()
            if current_loc == 'Lut Gholein':
                town_zone()
            else:
                location_art()
                zone_navigation_menu(enemy_zone, x, y)
                return False
        else:
            stash_menu()
            print('Type number to equip item or "R" to go backward')

def stash_menu():
    """
    Display stash menu
    """
    stash_sheet = SHEET.worksheet('stash').get_all_values()
    stash_limit = stash_sheet[2:9]
    print(f'Equipped:    {stash_sheet[1][0]}\n')
    print(' ' * 5 + 'Item' + ' ' * 12 + 'Attack' + ' '* 5 + '+Max Heath\n')
    for number, item in enumerate(stash_limit, 1):
        # Enumerates all items in stash and ensures correct positioning of the display
        print(str(number) + '.', item[0].title() + ' ' * (20 - len(item[0]) - len(item[1]) + 1), 
              item[1],' ' * (10 - len(item[2]) + 2), item[2])
    print('')
    if len(stash_sheet) > 2:
        print('Select a number to equip the weapon\n')
    else:
        print('You have no items to equip\n')
    print('E. Go back\n')

def return_to_town():
    zone_navigation_menu(enemy_zone, x, y)
    print('')
    print('Would you like to return to town?')
    while True:
        town_portal = input('Y/N:\n')
        clear()
        if town_portal.lower() == 'y':
            town_zone()
            
        elif town_portal.lower() == 'n':
            location_art()
            zone_navigation_menu(enemy_zone, x, y)
            return False
        else:
            location_art()
            zone_navigation_menu(enemy_zone, x, y)
            print('')
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
    print('W. Character Info')
    print('E. Open Stash')
    print('R. Visit Vendor\n')
    
def vendor():
    """
    Display items on sale and requests user input to purchase
    """
    global current_loc

    current_loc = 'Vendor'
    vendor_menu()
    while True:
        vendor_menu_select = input('')
        clear()
        if vendor_menu_select == '1':
            vendor_buy_menu()
            vendor_buy_menu_option()
            vendor_menu()
        elif vendor_menu_select == '2':
            vendor_sell_menu()
            vendor_sell_menu_option()
            clear()
            vendor_menu()
        elif vendor_menu_select == '3':
            vendor_gossip()
            vendor_gossip_back()
        elif vendor_menu_select.lower() == 'r':
            town_zone()
        else:
            vendor_menu()
            print('Type 1-3 to select a menu option')
            
def vendor_menu():
    """
    Display vendors menu options
    """
    location_art()
    print('1. Buy')
    print('2. Sell')
    print('3. Gossip\n')
    print('R. Go Back\n')


def vendor_buy_menu():
    """
    Display vendors menu options
    """
    global health_potion, hero_gold

    location_art()
    print('Your gold:' + ' ' * (7 - len(str(hero_gold)) + 1) + f'{hero_gold}')
    print('Health_potion:' + ' ' * (4 - len(str(health_potion))) + f'{health_potion}\n')
    print('1. Buy Health Potion        100 gold')
    print('\n')
    print('R. Go Back')
    print('')

def vendor_buy_menu_option():
    """
    Takes player input to navigate vendors buy menu
    """
    global health_potion, hero_gold

    while True:
        buy = input('\n')
        clear()
        vendor_buy_menu()
        if buy == '1':
            print('Would you like to buy Health Potion?')
            purchase_confirm = input('Y/N\n')
            if purchase_confirm.lower() == 'y':
                if hero_gold >= 100:
                    hero_gold -= 100
                    health_potion += 1
                    clear()
                    vendor_buy_menu()
                else:
                    clear()
                    vendor_buy_menu()
            elif purchase_confirm.lower() == 'n':
                clear()
                vendor_buy_menu()
            else:
                vendor_buy_menu()
        elif buy.lower() == 'r':
            clear()
            return False
        else:
            print('Press "1" to buy item or "R" to go back')

def vendor_sell_menu():
    """
    Display vendors sell menu options
    """
    global hero_gold, stash_sheet, stash_limit, num

    location_art()
    print('Your gold:' + ' ' * (7 - len(str(hero_gold)) + 1) + f'{hero_gold}\n')
    stash_sheet = SHEET.worksheet('stash').get_all_values()
    stash_limit = stash_sheet[2:]
    if len(stash_limit) > 0:
        for number, item in enumerate(stash_limit, 1):
            # Enumerates all items in stash and ensures correct positioning of the display
            print(str(number) + '.', item[0].title() + ' ' * (15 - len(item[0])), item[4])
        print('')
        num = number
        print(f'Enter number from 1 to {number} to sell\n')
    else:
        print('You have nothing to sell\n')
    print('R. Go Back\n')

def vendor_sell_menu_option():
    """
    Takes player input to navigate vendors sell menu
    """
    global health_potion, hero_gold, stash_sheet, num

    stash = SHEET.worksheet('stash')
    while True:
        sell = input('\n')
        clear()
        vendor_sell_input(sell, stash)
        return False

def vendor_sell_input(sell, stash):
    """
    Handles player input for vendor sell menu
    """
    global hero_gold, num

    if sell == '1' or sell == '2' or sell == '3' or sell == '4' or sell == '5' or sell == '6' or sell == '7':
        stash_sheet = SHEET.worksheet('stash').get_all_values()
        if 0 < int(sell) < len(stash_sheet):
            vendor_sell_menu()
            print(f'Would you like to sell {stash_sheet[int(sell)+1][0]}?')
            sale_confirm = input('Y/N\n')
            if sale_confirm.lower() == 'y':
                hero_gold += int(stash_sheet[int(sell)+1][4])
                remove_first = stash_sheet.pop(int(sell)+1)
                stash.clear()
                for row in stash_sheet:
                    stash.append_row(row)
                clear()
                vendor_sell_menu()
            elif sale_confirm.lower() == 'n':
                clear()
                vendor_sell_menu()
            else:
                vendor_sell_menu()
                print('Type "Y" to confirm the sale or "N" to cancel')
        else:
            vendor_sell_menu()
            print(f'Type number to sell item or "R" to go back')
    elif sell.lower() == 'r':
        clear()
        vendor_sell_menu()
    else:
        vendor_sell_menu()
        print(f'Type numbe to sell item or "R" to go backward')

def vendor_gossip():
    """
    Prints text that gives a hint to player
    """
    location_art()
    print('Someone stole the key for the main gate last night.')
    print('That bloody Radement must have send a goblin over.')
    print('Radement is imprisoned deep inside the sewers.')
    print('Only if there was anyone brave enough to confront him.\n')
    print('R. Go back\n')

def vendor_gossip_back():
    """
    Vendor gossip navigation
    """
    while True:
        back_to_menu = input('\n')
        clear()
        if back_to_menu == 'r':
            vendor()
        else:
            vendor_gossip()
            print('Type "4" to go back to menu')

def game_win_logo():
    """
    Display winning screen
    """
    print('▓██   ██▓ ▒█████   █    ██     █     █░ ██▓ ███▄    █ ')
    print(' ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▓█░ █ ░█░▓██▒ ██ ▀█   █ ')
    print('  ▒██ ██░▒██░  ██▒▓██  ▒██░   ▒█░ █ ░█ ▒██▒▓██  ▀█ ██▒')
    print('  ░ ▐██▓░▒██   ██░▓▓█  ░██░   ░█░ █ ░█ ░██░▓██▒  ▐▌██▒')
    print('  ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░░██▒██▓ ░██░▒██░   ▓██░')
    print('   ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒    ░ ▓░▒ ▒  ░▓  ░ ▒░   ▒ ▒ ')
    print(' ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░      ▒ ░ ░   ▒ ░░ ░░   ░ ▒░')
    print(' ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░      ░   ░   ▒ ░   ░   ░ ░ ')
    print(' ░ ░         ░ ░     ░            ░     ░           ░ ')
    print(' ░ ░                                                  \n')
    print('Would you like to continue the game?Y/N\n')

def game_win():
    while True:
        continue_game = input('\n')
        clear()
        if continue_game.lower() == 'y':
            return False
        elif continue_game.lower() == 'n':
            quit()
        else:
            game_win_logo()
            print('Type "Y" to continue the game and "N" to quit')

def character_info():
    """
    Display character info
    """
    global hero_stats, hero_gold

    location_art()
    stats()
    
    while True:
        go_back = input('\n')
        clear()
        location_art()
        stats()
        if go_back.lower() == 'w':
            clear()
            if current_loc == 'Lut Gholein':
                town_zone()
            else:
                location_art()
                zone_navigation_menu(enemy_zone, x, y)
                return False
        else:
            print('Press "W" to go back')
def stats():
    """
    Character stats
    """
    print(f'Health:    {hero_max_health}')
    print(f'Attack:    {hero_attack}')
    print(f'Potions    {health_potion}')
    print(f'Gold:      {hero_gold}\n')
    print('W. Go Back\n')

main()