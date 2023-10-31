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
    input()

title_and_greeting()