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
