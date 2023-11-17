def game_menu_display_top():
    """
    Displays top half of the main menu
    ASCII art was created with https://www.asciiart.eu/image-to-ascii
    """
    print('\n')
    print('                               ...:*@@@@@@@@@*:..      ')
    print('                             .*@@=..   =@. ..=@@*..    ')
    print('                          ..#@+.      .@@%.    .+@%..  ')
    print('                         .-@+.,-----------------,.+@=. ')
    print('                        .-@:  |    GAME MENU    |  .@+.')
    print('                        -@+@@@|                 |...:@-')

def game_menu_display_bottom():
    """
    Displays bottom half of the main menu
    ASCII art was created with https://www.asciiart.eu/image-to-ascii
    """
    print('                        @*   .|   2. Save Game  |+.  +@')
    print('                        @*    |   3. Load Game  |    +@')
    print('                        *%    |   4. Rules      |   .%#')
    print('                        :@:.  |   5. End game   |  .:@-')
    print('                        .-@:  "-----------------" .:@=.')
    print('                         .:@+..@@@+.     .:@@@*. .+@-. ')
    print('                           .*@%=.           .*@.+@#..  ')
    print('                             .+@@=....   ....=@@*.     ')
    print('                               ..-*@@@@@@@@@*-..       ')

def vendor_sell_menu_display(stash_limit):
    """
    Displays sell menu at vendor
    """
    print('         φäðœ‰~-                                                -~‰œðäφ    ')
    print('         ‘%  ╔════════════════════════════════════════════════════╗  %‘    ')
    for number, item in enumerate(stash_limit, 1):
            # Enumerates all items in stash and ensures correct positioning of the display
            print(' ' * 22, str(number) + '.', item[0].title() + ' ' * (25 - len(item[0])), item[4])
    print('         ‘%  ╚════════════════════════════════════════════════════╝  %‘    ')
    print('        ‘φäðœ‰~-                                                -~‰œðäφ‘   \n')
    print('                         Enter a number to sell item                       \n')

def vendor_sell_menu_empty():
    print('         φäðœ‰~-                                                -~‰œðäφ    ')
    print('         ‘%  ╔════════════════════════════════════════════════════╗  %‘    ')
    print('                           You have nothing to sell                        ')
    print('         ‘%  ╚════════════════════════════════════════════════════╝  %‘    ')
    print('        ‘φäðœ‰~-                                                -~‰œðäφ‘   \n')

def vendor_buy_menu_art():
    """
    Display vendors menu options
    """
    print('         φäðœ‰~-                                                -~‰œðäφ    ')
    print('         ‘%  ╔════════════════════════════════════════════════════╗  %‘    ')
    print('                      1. Buy Health Potion        100 gold                 ')
    print('         ‘%  ╚════════════════════════════════════════════════════╝  %‘    ')
    print('        ‘φäðœ‰~-                                                -~‰œðäφ‘   \n')
    print('\n')
    print('R. Go Back')
    print('')

def vendor_menu_main():
    """
    Display main vendor menu
    """
    print('\n')
    print('                   φäðœ‰~-                             -~‰œðäφ   ')
    print('                   ‘%  ╔════════════════════════════════╗  %‘    ')
    print('                    δ  ║        1. Buy Weapon           ║  δ     ')
    print('                       ║        2. Sell Items           ║        ')
    print('                    δ  ║        3. Gossip               ║  δ     ')
    print('                   ‘%  ╚════════════════════════════════╝  %‘    ')
    print('                 ‘φäðœ‰~-                              -~‰œðäφ‘\n')
    print('R. Go Back')

def ingame_menu():
    """
    In game menu selection
    """
    print('             1. Go to Sewers                      Q. Open Menu')
    print('             2. Go to Dessert                     W. Character Info')
    print('                                                  E. Open Stash')
    print('                                                  R. Visit Vendor\n')
    