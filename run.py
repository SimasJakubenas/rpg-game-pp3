import gspread, random, os
from google.oauth2.service_account import Credentials
from modules.game_classes import Character, Hero, Enemy, Game_flow_bool, Location, Worksheets
from modules.ascii_art import title_and_greeting, game_win_logo, game_loso_logo
from modules.game_text import game_lore, game_rules, vendor_gossip
from modules.menus import game_menu_display_top, game_menu_display_bottom, vendor_sell_menu_display
from modules.menus import vendor_sell_menu_empty, vendor_buy_menu_art, vendor_menu_main, ingame_menu, stash_menu_display

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
initial_state = Game_flow_bool(False, False, False, False, True, False, False, False, False, False)
# Assigns worksheets from a spreadsheet to Worksheet class
worksheets = Worksheets('sewers', 'dessert', 'chars', 'items', 'shop', 'stash', 'save', 'stash_save')
# Location class inital values
location = Location('', '', 0, 0 )
# Initial hero stats
character_list = SHEET.worksheet('chars').get_all_values()
hero = tuple(character_list[1])
hero_stats = Hero(*hero)
item_list = SHEET.worksheet('items').get_all_values()
# Symbols used in health bars
full_life = '█'
empty_life = '_'

def main():
    """
    Main game function
    """
    title_and_greeting()
    clear()
    game_menu_display()
    game_menu_select()

def game_menu_display():
    """
    Calls for game menu and requires user input to select menu item
    ASCII art was created with https://www.asciiart.eu/image-to-ascii
    """
    game_menu_display_top()
    if initial_state.hero_created == False:
        print('                        #%..:@|   1. New Game   |@@@+%%')
    else:
        print('                        #%..:@|   1. Continue   |@@@+%%')
    game_menu_display_bottom()

def game_menu_select():
    """
    Selects menu option based of user input
    """
    while True:
        menu_item = input('\n')
        clear()
        game_menu_display()
        # Starts game
        if menu_item == '1':
            start_game()
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
        # Game rules   
        elif menu_item == '4':
            clear()
            game_rules()
            game_rules_back()
        # Game quit
        elif menu_item == '5':
            menu_item = 'quit'
            menu_option(menu_item)
        else:
            print('')
            print('Select Menu Option by entering a number 1-5')

def start_game():
    """
    Starts gane when player select 'New Game' option in menu
    This imput serves as 'Continue' logic checks if the game been started already
    """
    menu_item = 'start'
    if initial_state.alive == False:
        if initial_state.hero_created == False:
            menu_option(menu_item)
        else:
            town_zone()
    else:
        clear()
        location_art()
        if location.current_location == 'Lut Gholein':
            ingame_menu()
        else:
            zone_navigation_menu()
        return False

def menu_option(menu_item):
    """
    Calls appropriate functions that corresponds with players input 
    """
    print('')
    while True:
        want_to_quit = input(f"Do you want to {menu_item} the game?Y/N\n")
        clear()

        if want_to_quit.lower() == 'y':
            confirmed_menu_selection(menu_item)
        elif want_to_quit.lower() == 'n':
            game_menu_display()
            return False
        else:
            game_menu_display()
            print('')
            print('Type in "y" to save or "N" to go back to menu')

def confirmed_menu_selection(menu_item):
    """
    Starts corresponding game mode based on user input
    """
    if menu_item == 'start':
        initial_state.alive = True
        initial_state.hero_created = True
        game_lore()
        clear()
        # Starting new game clears stash worksheet content
        SHEET.values_clear("stash!A2:F10000")
        # A space holder for equipped weapon
        SHEET.worksheet(worksheets.stash).append_row(['Stick', '0', '0', '0', '5', '0'])
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
        initial_state.loaded_game = True
        load_game()
        clear()
        town_zone()
    if menu_item == 'quit':
        quit()

def save_game():
    """
    Saves heros stats by pushing hero stats to a google spreadsheet
    Saves aquired items to a google spreadsheet
    """
    print('Game saving please wait....')
    hero_stats_dict = vars(hero_stats)
    hero_stats_list = list(hero_stats_dict.values())
    SHEET.worksheet(worksheets.save).append_row(hero_stats_list)

    get_items = SHEET.worksheet(worksheets.stash).get_all_values()
    SHEET.worksheet(worksheets.stash_save).clear()
    for item in get_items:
        SHEET.worksheet(worksheets.stash_save).append_row(item)

def load_game():
    """
    Loads the game by pulling character stats from save worksheet
    Transfers save items to a relevant worksheet
    """
    save_file = SHEET.worksheet(worksheets.save).get_all_values()
    while True:
        if len(save_file) > 1:
            print('Game loading please wait....')
            last_save = save_file[-1]
            hero_stats.health = int(last_save[2])
            hero_stats.max_health = int(last_save[2])
            hero_stats.attack = int(last_save[3])
            hero_stats.gold = int(last_save[4])
            hero_stats.health_potion = int(last_save[5])

            load_items_list = SHEET.worksheet(worksheets.stash_save).get_all_values()
            SHEET.worksheet(worksheets.stash).clear()
            for item in load_items_list:
                SHEET.worksheet(worksheets.stash).append_row(item)
            return False
        else:
            game_menu_display()
            print('You need to save the game first!')
            game_menu_select()

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
            clear()
            game_rules()
            print('Type "4" to go back to menu')

def town_zone():
    """
    Starting game zone with that prompts the player to navigate the game
    """
    location.current_location = 'Lut Gholein'
    initial_state.sewers = False
    initial_state.dessert = False
    location_art()
    ingame_menu()
    # Loaded_game boolen used only to control positioning of the text bellow
    if initial_state.loaded_game == True:
        print('The game was loaded...')
    initial_state.loaded_game = False
    while True:
        navigate_town = input('\n')
        clear()
        if navigate_town == '1':
            initial_state.sewers = True
            enemy_zone_navigation()
        elif navigate_town == '2':
            if initial_state.key:
                initial_state.dessert = True
                enemy_zone_navigation()
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

def enemy_zone_navigation():
    """
    Pulls sewers map from the spreadsheet and defines movement
    """
    if initial_state.sewers == True:
        location.enemy_zone = SHEET.worksheet(worksheets.sewers_map).get_all_values()
        location.x = 2
        location.y = 2
    if initial_state.dessert == True:
        location.enemy_zone = SHEET.worksheet(worksheets.dessert_map).get_all_values()
        location.x = 1
        location.y = 1
    location.current_location = location.enemy_zone[location.x][location.y]
    location_art()
    zone_navigation_menu()
    while True:
        location.current_location = location.enemy_zone[location.x][location.y]
        if (location.current_location != 'Dungeon Gate') and (location.current_location != 'Town Gate'):
            not_town_portal()
        else:
            if initial_state.fight:
                initial_state.fight = False
                location_art()
                return_to_town()
        zone_navigation_menu_input()

def not_town_portal():
    """
    Checks if a tile the players is on is a town portal
    """
    if location.current_location == 'Sewers Hideout':
        if initial_state.treasure_chest:
            location_art()
            zone_navigation_menu()
            print('')
            print('You found 200 gold!')
            hero_stats.gold += int(character_list[5][3])
            initial_state.treasure_chest = False
            initial_state.fight = False
        else:
            battle()
    if initial_state.fight:
        location_art()
        battle()
        hero_stats.health_potion += 1
        initial_state.fight = False

def zone_navigation_menu_input():
    """
    Takes user input to navigate enemy zone
    """
    zone_controls = input('\n')
    clear()
    # 'And' operators prevents game from crashing if player tries to move out of map
    if zone_controls == '1' and location.x > 0:
        location.x -= 1
        initial_state.fight = True
    elif zone_controls == '2' and location.y < len(location.enemy_zone[location.x]) - 1:
        location.y += 1
        initial_state.fight = True
    elif zone_controls == '3' and location.x < len(location.enemy_zone) - 1:
        location.x += 1
        initial_state.fight = True
    elif zone_controls == '4' and location.y > 0:
        location.y -= 1
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
        zone_navigation_menu()
        print('')
        print('Use numers 1-4 to navigate the map')

def zone_navigation_menu():
    """
    Calls enemy_zone_menu methot from Location class
    Shows message if players stash is full and they decide to not replace an old item with the new one
    """
    location.enemy_zone_menu()
    
    if initial_state.replace:
        print(f'You left your loot behind')
    initial_state.replace = False

def battle():
    """
    Battle function determines an enemy encounter depending on map area
    Loops through a fight until either player or enemy dies
    Provide player with battle options
    """
    # Caps heros health at max_health if weapon is swpped with a one that has less max_health
    if hero_stats.health > hero_stats.max_health:
        hero_stats.health = hero_stats.max_health
    # Selects enemies from a list based on location
    if initial_state.sewers == True:
        enemy_list = slice(2, 7)
    if initial_state.dessert == True:
        enemy_list = slice(7, 19)
    while initial_state.fight: 
        enemy = tuple(random.choice(character_list[enemy_list]))
        if enemy[4] == location.current_location:
            # Once 'Radement' is killed stepping on his tile will create random enemy
            if (enemy[0] == 'Radement' and initial_state.key == True) \
                or (location.current_location == 'Sewers Hideout' and initial_state.treasure_chest == False):
                enemy_list = slice(2, 5)
                enemy = tuple(random.choice(character_list[enemy_list]))
            enemy_stats = Enemy(*enemy)
            initial_state.fight = False
            print(f'You have been attacked by {enemy[0]}')
    # Loops the fight until either player's or enemy's health reaches 0
    while enemy_stats.health > 0:
        print(f'{enemy_stats.name} has done {enemy_stats.attack} damage to you')
        hero_stats.health -= enemy_stats.attack

        if hero_stats.health <= 0:
            game_loso_logo()
            initial_state.alive = False
            input('\n')
            clear()
            main()
        battle_menu(enemy_stats)

        battle_options(enemy_stats)

def battle_menu(enemy_stats):
    """
    Display health of player and enemy and display menu options in battle
    Health bars were made following and altering to fit project https://www.youtube.com/watch?v=0e2DexQlDYk tutorial
    How to break up print method was taken from 'noddy' answer in https://stackoverflow.com/questions/45965007/multiline-f-string-in-python
    """
    current_health_bar = round((hero_stats.health / hero_stats.max_health) *100) // 4
    current_health_bar_enemy = round((enemy_stats.health / enemy_stats.max_health) *100) // 4
    lost_life_bar = 25 - current_health_bar
    lost_life_bar_enemy = 25 - current_health_bar_enemy
    print(' Your Life', ' ' * (52 - len(enemy_stats.name)), f"{enemy_stats.name}'s life")
    print(
        f'{current_health_bar * full_life}{lost_life_bar * empty_life}║',
        ' ' * (3 - len(str(hero_stats.health))),
        f'{hero_stats.health}/{hero_stats.max_health}',
        ' ' * (13 - len(str(enemy_stats.health))),
        f'{enemy_stats.health}/{enemy_stats.max_health} ║'
        f'{lost_life_bar_enemy * empty_life}{current_health_bar_enemy * full_life}\n')
    print('1. Attack')
    print('2. Use Potion')
    print('')

def battle_options(enemy_stats):
    """
    Takes user input of a battle option and runs corresponding action
    """
    while True:
        battle_option = input('\n')
        clear()
        location_art() 
        # Option to attack
        if battle_option == '1':
            battle_option_attack(enemy_stats)
            return enemy_stats.health
        # Option to heal
        elif battle_option == '2':
            if hero_stats.health_potion > 0:
                hero_stats.health += 50
                if hero_stats.health > hero_stats.max_health:
                    hero_stats.health = hero_stats.max_health
                hero_stats.health_potion -= 1
                print('You gained 50 life!')
                return hero_stats.health
            else:
                battle_menu(enemy_stats)
                print('You have no health pots')
        else:
            if initial_state.first_attack == False:
                print(f'You have been attacked by {enemy[0]}')
            else:
                print(f'You have done {hero_stats.attack} damage to {enemy_stats.name}')
            print(f'{enemy_stats.name} has done {enemy_stats.attack} damage to you')
            battle_menu(enemy_stats)
            print('Type a number 1-n to select battle option')

def battle_option_attack(enemy_stats):
    """
    Deals damage to enemy health
    Checks for game bosses and runs corresponding methods
    """
    initial_state.first_attack = True
    enemy_stats.health -= hero_stats.attack
    print(f'You have done {hero_stats.attack} damage to {enemy_stats.name}')
    if enemy_stats.health <= 0:
        print(f'{enemy_stats.name} has fallen and dropped {enemy_stats.gold} gold')
        item_drop()
        print('')
        zone_navigation_menu()
        hero_stats.gold += enemy_stats.gold
        print('')
        if enemy_stats.name == 'Radement':
            initial_state.key = True
            clear()
            location_art()
            return_to_town()
        if enemy_stats.name == 'Duriel':
            game_win_logo()
            game_win()

def item_drop():
    """
    Draws data from items worksheet for a chance to aquire item
    If stash is over max capacity prompts user to replace first item in the stash with a new one
    """
    stash_sheet = SHEET.worksheet(worksheets.stash).get_all_values()
    weapon_list = item_list[3:]
    for weapon in weapon_list:
        if float(weapon[-1]) >= random.random():
            print(f'You found {weapon[0]}\n')
            SHEET.worksheet(worksheets.stash).append_row(weapon)
            stash_sheet.append(weapon)
        # When stash over max capacity prompts user to replace first item in the stash with a new one
        while len(stash_sheet) > 8:
            remove_item = input(f'Not enough space in stash would you like to remove {stash_sheet[1][0]}?Y/N\n')
            clear()
            if remove_item.lower() == 'y':
                remove_first = stash_sheet.pop(1)
                SHEET.worksheet(worksheets.stash).clear()
                for row in stash_sheet:
                    SHEET.worksheet(worksheets.stash).append_row(row)
                location_art()
            elif remove_item.lower() == 'n':
                del stash_sheet[-1]
                SHEET.worksheet(worksheets.stash).clear()
                for row in stash_sheet:
                    SHEET.worksheet(worksheets.stash).append_row(row)
                initial_state.replace = True
                location_art()
            else:
                location_art()
                print(f'You found {weapon[0]}\n')
                print(f'Press "Y" to replace {stash_sheet[1][0]} or "N" to pass on this item')

def stash_open():
    """
    Display aquired items
    Pull and display relevant data from 'stash' spreadsheet
    """
    location_art()
    stash_menu()
    while True:
        equip = input('\n')
        clear()
        location_art()
        if equip == '1' or equip == '2' or equip == '3' or equip == '4' or equip == '5' or equip == '6':
            stash_sheet = SHEET.worksheet(worksheets.stash).get_all_values()
            if 0 < int(equip) < len(stash_sheet):
                equip_weapon(equip, stash_sheet)
            else:
                print(f'Type number to equip item or "R" to go back')
        elif equip.lower() == 'e':
            clear()
            if location.current_location == 'Lut Gholein':
                town_zone()
            else:
                location_art()
                zone_navigation_menu()
                return False
        else:
            stash_menu()
            print('Type number to equip item or "R" to go backward')

def equip_weapon(equip, stash_sheet):
    """
    Haddles user input to equip weapon
    if weapon is equiped the stash worksheet is appended appropreately
    """
    stash_menu()
    print(f'Would you like to equip {stash_sheet[int(equip)+1][0]}?')
    while True:
        equip_confirm = input('Y/N\n')
        if equip_confirm.lower() == 'y':
            stash_limit = stash_sheet[1:9]
            equipped_weapon = stash_limit.pop(int(equip))
            SHEET.values_clear("stash!A2:F10000")
            hero_stats.attack = int(hero[2]) + int(equipped_weapon[1])
            hero_stats.max_health = int(hero[1]) + int(equipped_weapon[2])
            SHEET.worksheet(worksheets.stash).append_row(equipped_weapon)
            for row in stash_limit:
                SHEET.worksheet(worksheets.stash).append_row(row)
            stash_sheet = SHEET.worksheet(worksheets.stash).get_all_values()
            clear()
            stash_open()
        elif equip_confirm.lower() == 'n':
            clear()
            stash_open()
        else:
            clear()
            location_art()
            stash_menu()
            print('Type "Y" to confirm to equip or "N" to cancel')

def stash_menu():
    """
    Display stash menu
    """
    stash_sheet = SHEET.worksheet(worksheets.stash).get_all_values()
    stash_limit = stash_sheet[2:9]
    stash_menu_display(stash_sheet, stash_limit)
    if len(stash_sheet) > 2:
        print(' ' * 20, 'Select a number to equip the weapon\n')
    print('E. Go back')

def return_to_town():
    zone_navigation_menu()
    print('')
    print('Would you like to return to town?')
    while True:
        town_portal = input('Y/N:\n')
        clear()
        if town_portal.lower() == 'y':
            town_zone()
            
        elif town_portal.lower() == 'n':
            location_art()
            zone_navigation_menu()
            return False
        else:
            location_art()
            zone_navigation_menu()
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
    print(' ' * 22, '-.;:~■-■---' + '~' * len(location.current_location) + '---■-■~:;.-')
    print(' ' * 28, f'>>►► {location.current_location} ◄◄<<     ')
    print(' ' * 22, '-.;:~■-■---' + '~' * len(location.current_location) + '---■-■~:;.-\n')

def vendor():
    """
    Display items on sale and requests user input to purchase
    """
    location.current_location = 'Vendor'
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
            location_art()
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
    vendor_menu_main()

def vendor_buy_menu():
    """
    Display hero's gold, health potions and available items on sale
    """
    location_art()
    print(' ' * 30, 'Your gold:' + ' ' * (7 - len(str(hero_stats.gold)) + 1) + f'{hero_stats.gold}')
    print(' ' * 30, 'Health_potion:' + ' ' * (4 - len(str(hero_stats.health_potion))) + f'{hero_stats.health_potion}\n')
    vendor_buy_menu_art()

def vendor_buy_menu_option():
    """
    Takes player input to navigate vendors buy menu
    """
    while True:
        buy = input('\n')
        clear()
        vendor_buy_menu()
        if buy == '1':
            vendor_buy_select()
        elif buy.lower() == 'r':
            clear()
            return False
        else:
            print('Press "1" to buy item or "R" to go back')

def vendor_buy_select():
    """
    """
    print('Would you like to buy Health Potion?')
    while True:
        purchase_confirm = input('Y/N\n')
        clear()
        if purchase_confirm.lower() == 'y':
            if hero_stats.gold >= 100:
                hero_stats.gold -= 100
                hero_stats.health_potion += 1
                clear()
                vendor_buy_menu()
                vendor_buy_menu_option()
            else:
                clear()
                vendor_buy_menu()
                print('Not enough gold')
                vendor_buy_menu_option()
        elif purchase_confirm.lower() == 'n':
            vendor_buy_menu()
            vendor_buy_menu_option()
        else:
            vendor_buy_menu()
            print('Type "Y" to confirm or "N" no cansel purchase')

def vendor_sell_menu():
    """
    Display vendors sell menu options
    """
    location_art()
    print(' ' * 30, 'Your gold:' + ' ' * (7 - len(str(hero_stats.gold)) + 1) + f'{hero_stats.gold}\n')
    stash_sheet = SHEET.worksheet(worksheets.stash).get_all_values()
    stash_limit = stash_sheet[2:]
    if len(stash_limit) > 0:
        vendor_sell_menu_display(stash_limit)
    else:
        vendor_sell_menu_empty()
    print('R. Go Back')

def vendor_sell_menu_option():
    """
    Takes player input to navigate vendors sell menu
    """
    while True:
        sell = input('\n')
        clear()
        vendor_sell_input(sell)
        return False

def vendor_sell_input(sell):
    """
    Handles player input for vendor sell menu
    """
    if sell == '1' or sell == '2' or sell == '3' or sell == '4' or sell == '5' or sell == '6' or sell == '7':
        stash_sheet = SHEET.worksheet(worksheets.stash).get_all_values()
        if 0 < int(sell) < len(stash_sheet):
            vendor_sell_menu()
            print(f'Would you like to sell {stash_sheet[int(sell)+1][0]}?')
            vendor_sell_select(sell, stash_sheet)
        else:
            vendor_sell_menu()
            print(f'Type number to sell item or "R" to go back')
    elif sell.lower() == 'r':
        clear()
        vendor_sell_menu()
    else:
        vendor_sell_menu()
        print(f'Type numbe to sell item or "R" to go backward')

def vendor_sell_select(sell, stash_sheet):
    """
    Verifies user input to sell an item
    """
    while True:
        sale_confirm = input('Y/N\n')
        if sale_confirm.lower() == 'y':
            hero_stats.gold += int(stash_sheet[int(sell)+1][4])
            remove_first = stash_sheet.pop(int(sell)+1)
            SHEET.worksheet(worksheets.stash).clear()
            for row in stash_sheet:
                SHEET.worksheet(worksheets.stash).append_row(row)
            clear()
            vendor_sell_menu()
            vendor_sell_menu_option()
        elif sale_confirm.lower() == 'n':
            clear()
            vendor_sell_menu()
            vendor_sell_menu_option()
        else:
            clear()
            vendor_sell_menu()
            print('Type "Y" to confirm the sale or "N" to cancel')

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
            location_art()
            vendor_gossip()
            print('Type "4" to go back to menu')

def game_win():
    """
    Request and control user input to continue the game when game is won
    """
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
    location_art()
    hero_stats.stats()
    
    while True:
        go_back = input('\n')
        clear()
        location_art()
        hero_stats.stats()
        if go_back.lower() == 'w':
            clear()
            if location.current_location == 'Lut Gholein':
                town_zone()
            else:
                location_art()
                zone_navigation_menu()
                return False
        else:
            print('Press "W" to go back')

main()