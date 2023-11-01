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

    sewers_zone = SHEET.worksheet('sewers').get_all_values()

    print('Welcome to the town of Lut Gholein! What would you like to do?')
    print('1. Go to Sewers')
    navigate_town = input()
    while True:
        if navigate_town == '1':
            print(f'You have entered {sewers_zone[2][2]}')
        elif navigate_town == '2':
            pass
        elif navigate_town == '3':
            pass
        elif navigate_town == '4':
            pass
        else:
            print('Enter a number 1-4 to select your destination')

title_and_greeting()