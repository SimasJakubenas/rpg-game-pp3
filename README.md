#Tal Rasha

![image](https://github.com/SimasJakubenas/rpg-game-pp3/assets/138577499/8ddb2b0e-50f0-408b-93a6-fc78b4818721)

Developer: Simas Jakubenas

Tal Rasha is a RPG style game that is inspired by a classic Diablo II game. The players quest is to navigate the map, find Duriel and destroy him once and for all!

A link to deployed game
https://tal-rasha-rpg-6583f66e1480.herokuapp.com/

## Contents
[UX Design](#ux-design)
* [The Strategy Plane](#the-strategy-plane)
* [The Scope Plane](#the-scope-plane)
* [The Structure Plane](#the-structure-plane)
* [The Skeleton Plane](#the-skeleton-plane)
* [The Surface Plane](#the-surface-plane)
[Features](#features)
* [Current Features](#current-features)
* [future Features](#future-features)
[Technologies Used](#technologies-used)
* [Languages used](#languages-used)
* [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)
[Deployment & Local Development](#deployment--local-development)
* [To deploy Heroku pages](#to-deploy-using-github-pages)
* [Local Development](#local-development)
  * [How to Fork](#how-to-fork)
  * [How to Clone](#how-to-clone)
[Testing](#testing)
* [Solved Bugs](#solved-bugs)
* [Known Bugs](#known-bugs)
[Credits](#credits)
* [Code used](#code-used)
* [Content](#content)
* [Media](#media)
* [Acknowledgments](#acknowledgments)

# Tal Rasha

![image](https://github.com/SimasJakubenas/rpg-game-pp3/assets/138577499/8ddb2b0e-50f0-408b-93a6-fc78b4818721)

Developer: Simas Jakubenas

Tal Rasha is a RPG style game that is inspired by a classic Diablo II game. The players quest is to navigate the map, find Duriel and destroy him once and for all!

A link to deployed game
https://tal-rasha-rpg-6583f66e1480.herokuapp.com/

## UX Design

### The Strategy Plane

With this project I'll be attempting to create a simple yet functional RPG type game that is run in terminal. The game is themed based on a classic game (Diablo II) and will have standart RPG mechanics like exploring the map, battling enemies and upgrading your character.

#### Target Audience

Main target audience for this project is millennials who grew up playing classic games like Diablo II. This game will spark a sense of nostalgia in players mind and captivate them throughout the gameplay. Having said that anyone that loves RPG games or gaming in general will have a fun time playing 'Tal Rasha'.

#### Problem Statement

Spending time playing games is almost never an option when you become an adult :(. Especially RPG genre games that requires a player to put in hours uppon hours of gameplay. 

#### Competitor Annalisys

While this project is nowhere near Diablo II or it's moderated versions (some of which are still going strong to this day) it still offers few advantages:

- You can complete it quite quickly
- No downloads or registration required

### The Scope Plane

#### User Stories

##### First Time User Goals:

- FTU_01 As a first-time user, I want to discern what kind of game this is  immediately, so that I know I'm in the right place
- FTU_02 As a first-time user, I want to be able to navigate the game flow intuitively, so that I can enjoy playing it
- FTU_03 As a first-time user, I want to play an RPG type game, so that I have a fun way to pass my time
- FTU_04 As a first-time user, I want to be faced with a level of difficulty, so that I can be engaged by the gameplay 
- FTU_05 As a first-time user, I want to see the progression of the game based on my decisions, so that I can be motivated to continue playing.
- FTU_06 As a first-time user, I want to be able to complete the game, so that I feel rewarded

##### Returning User Goals:

- RU_01 As a returning user, I want to be able to save/load the game, so I can continue playing another time
- RU_02 As a returning user, I want to see if there's an update to the game, so I can replay it
- RU_03 As a returning user, I want to explore all areas, so that I can encounter all the enemies.

##### Developer Goals:

- SD_01 As a developer, I want to provide a fun and engaging RPG style game, so that others would be able to enjoy it.
- SD_02 As a developer, I want to save game content on google spreadsheets, so that I can add more content without changing the code.
- SD_03 As a developer, I want to have a platform on  which I can build continuosly, so that I could realize my passion.

##### Future Development:

- FTU_07 As a first-time user, I want to be able to hear sounds of the game, I that I could be engaged more.
- FTU_08 As a first-time user, I want to be able to select a different character of the game, so that I'm more inclined to repeat the game.
- RU_04 As a returning user, I want to be able to change game difficulty, so that I could face a greater challenge.

#### Content Requirements and Feature Sets

In the table bellow i tried to extract requirements for the site from user and developer stories and match those requirements with a set of features. Moreover I tried to follow agile approach where project features were split into sprints allowing for an early deployment of the project with basic controls of the game running. This permits the user the ability to test the game while I work on the second sprint. The 3rd sprint is dedicated towards future development.

| Requirement | Feature | sprint |
| -- | -- | -- |
| A functioning and fun RPG type game (FTU_03, FTU_04, FTU_05, FTU_06, RU_03, SD_01) | 1. A starting town | 1 |
| | 2. A shop for items/potions | 2 |
| | 3. A stash to store items | 3 |
| | 4. A map progression through the game | 1/2 |
| | 5. A change to encounter enemies while navigating the map | 1 |
| | 6. Battle sequence | 1 |
| | 7. Chance to aquire items after the fight | 2 |
| | 8. Boss fight at the end to win the game | 2 |
| An intuitive game menu (FTU_02, RU_01) | 9. Option to start the game| 1 |
| | 10. Option to end the game | 1 |
| | 11. Game rules | 2 |
| | 12. Option to save/load the game | 3 |
| Game title window (FTU_01) | 13. ASCII art for game title | 2 |
| | 14. Greeting message | 1 |
| Character selection (RU_02, FTU_08) | 15. Introduce different playable characters | 3 |
| Game difficulty level (RU_02, RU_04) | 16. Introduce game difficulty selection | 3 |
| Utilising google sheets (SD_02) | 17. Storing game content on google spreadsheets | 1 |
| Deployment on Heroku (SD_03) | 18. Deployed on Heroku | 1 |
| Adding game sounds/ASCII art (FTU_07) | 19. Add game music | 3 |
| | 20. Add game sounds | 3 |
| | 21. Add ASCII art to improve the visuals of the game | 3 |

### The Structure Plane

This game has standart features and game flow of a classic RPG genre game. The game is controlled via user imputs.
Uppon launching the game player is presented with a 
ASCII art generated image of the name of the game and 
a lore of the game to introduce the player to the game.

#### Game Architecture

Player is shown main menu with ouptions to start the game, save the game, load the game, read game rules and quit. menu is accessible at any point in the game (accept for when a player is in a balttle).
When game is started the player is in the starting zone or 'The town' where they have an option to :
* visit vendor (to buy and sell items)
* visit to open stash which has all the aquired items on display (you aslo can swap your current weapon here)
* check player info
* travel to one of the enemy zones (one of which is only accessible after killing a mini boss from the first zone)
Killing the boss in the second zone wins the game

### The Skeleton Plane

Initial flowchart of the game
![image](https://github.com/SimasJakubenas/rpg-game-pp3/assets/138577499/d89979b9-3c61-4cc8-9441-85322313c891)

For the most part I stuck with the initial chart. There is a couple noticible changes though:
* the stash is accessible from enemy zones also
* the addition to mini boss in the first zone

A google spreadsheet was used to store all the data (map tiles, items, hero and enemy stats etx...) on separate worksheets. This allows for the introduction of API's to the project while simultaneously providing a way to expand game content with very minimal code adjusments. A win win situation!

![Characters PDF](documentation/chars.pdf)

![Dessert Map PDF](documentation/dessert.pdf)

![Sewers Map PDF](documentation/sewers.pdf)

![Items PDF](documentation/items.pdf)

![Save game PDF](documentation/save.pdf)

![Save stash PDF](documentation/stash_save.pdf)

Great deal of effort was dedicated towards handling user inputs. All incorect inputs should return a message to the player (unless I missed something) with the exception of a handful of empty inputs (like the one when the game is launched) that are just there to stop loops and do not require the player to enter anything specific other than to hit 'enter' key.

Another pain of mine was the positioning of all text. It's rather unnatural for the terminal to display the text in the order I wanted so it took alot of tweaking and even utilising boolean logic in some cases. Although it brought me to the brink of insanity I'm happy with the end result.

### The Surface Plane

As this is a terminal game it's very limited in terms of visual appearance, however I tried to utilize the use of 'ASCII' arc to make the game more appealing to the player and break up the monotony of text.

Game Name, You Win and Game Over 'images' created with ASCII text generator (link in credits section of this README)

![image](https://github.com/SimasJakubenas/rpg-game-pp3/assets/138577499/22f6246a-12c0-402d-9168-e6574a979d08)

Also 'ASCII' art was used for images in town and enemy zones and of items that are aquired during battle.

![image](https://github.com/SimasJakubenas/rpg-game-pp3/assets/138577499/95e8e83a-1e61-4730-9e22-c9cac86b27ee)

Vendor, Stash and Character Info, game rules and game lore menus I styled myself

![image](https://github.com/SimasJakubenas/rpg-game-pp3/assets/138577499/decafc3d-e3b5-4a8b-8ae8-13545846152e)

I used a youtube tutorial to create 'health bars' for battle (credited in README)

![image](https://github.com/SimasJakubenas/rpg-game-pp3/assets/138577499/9c809e1d-ef3f-419f-b5ce-4bc4419f7c99)

## Features

All featured have numbers assigned to them which are linked to the requirement table in the scope plane above.

### Current Features

#### Game Title and Greeting
13, 14

Game title is is presented in a bold image to attract atention and the player is also greeted with a message that describes the game.

![image](https://github.com/SimasJakubenas/rpg-game-pp3/assets/138577499/3fb40ad3-0ea0-45e9-ab63-bb17de3c2a8f)

#### Main Menu
9, 10, 11, 12, 17

Gives options to:
* Start Game(9). As stated it starts a new game (Note that this option is replaced with 'Continue' when the game has been started already)
* Save Game(12). Saves the game by storing current character stats and aquired items on worksheets(17). Only available if the game has been started already. Currently the 'save file' is common for anyone playing the game however in the future I'm planning to take players name as input at the launch of the game and create separate worksheets using that input
* Load Game(12). Loads the game by pulling character info and stash data from corresponding worksheets(17). Only available if game has been saved already.
* Rules(11). Displays rules of the game
* Quit Game(10). Terminates the game

![image](https://github.com/SimasJakubenas/rpg-game-pp3/assets/138577499/91d111f2-d25f-466b-a345-581ffde347bc)

#### Game Lore
14

Introduces the player to the game further by giving them some background information

![image](https://github.com/SimasJakubenas/rpg-game-pp3/assets/138577499/f9c47b9d-295e-4c83-b5bb-95d378c764ac)

#### Starting Town
1, 2, 3, 4

Main game area that grants access to enemy zones(4), vendor(2), stash(4) and character info

![image](https://github.com/SimasJakubenas/rpg-game-pp3/assets/138577499/39750134-ad88-4c2d-8ef1-1f2cf39c529d)

#### Vendor
2

Game Vendor(2) options to buy, sell and listen to gossip

![image](https://github.com/SimasJakubenas/rpg-game-pp3/assets/138577499/043956f1-4bcf-4f2f-8e49-10fa72e73a94)

Buy window is limited to health potions only as I ran out of time to introduce items being sold. Buying health potion reduces the amount of gold player has by a specified amount and increases health potion count by 1.

![image](https://github.com/SimasJakubenas/rpg-game-pp3/assets/138577499/7d60a241-05e3-4f6a-9173-49f9c9c34929)

Selling window reveals all the items currently in the stash. item is sold by selecting the number beside it. Once item is sold it is removed from the list and heros gold is increased by the amount specified.

![image](https://github.com/SimasJakubenas/rpg-game-pp3/assets/138577499/1eae20aa-7a3d-44c2-8277-432468462945)

Gossip window gives player a hint how to advance to dessert zone

![image](https://github.com/SimasJakubenas/rpg-game-pp3/assets/138577499/6b645acd-1f32-42e5-b096-1abccf3be1e7)

#### Stash
3

Displays all the items the player currently has. Also displays the equipped weapon. Player can change the equipped weapon by selecting it's number. Some things to note:
* equipped weapon doesn't appear in vendors sell menu
* re-equiping weapons privides the player a means to organise the stash as the un-equipped item is places in the first slot of the stash(3). This comes in handy when maximum capacity of stash is reached (which is 6)
With any new item obtained the player will be presented with a choice tothrow out the first item.

![image](https://github.com/SimasJakubenas/rpg-game-pp3/assets/138577499/fc28da16-d788-4b42-b53e-2e6314a0e461)

#### Character Info

Displays character stats. Most notably health potion count which currently is not displayed anywhere else.

![image](https://github.com/SimasJakubenas/rpg-game-pp3/assets/138577499/bf66a702-fb80-4fa3-8998-235cfabb3280)

#### Enemy Zone Navigation
4

Player is presented with options to go to 4 cardinal directions(4). Player moves through the map by selecting a number from 1 to 4. Once the map 'edge' is reached the option to go to that direction is hidden.
Player can also access game menu, character info and stash while navigating.

![image](https://github.com/SimasJakubenas/rpg-game-pp3/assets/138577499/f269cfa5-dcd8-412b-aa3b-647c242d1a7e)

#### Enemy Encounter and Battle Sequence
5, 6

While player navigates the map they encounter(5) enemies on every tile. Diffent map tiles contains different enemies. Players movement triggers a battle(6). Enemy hits a player which in turn reduces playes health bar. Player has two options:
* attack - reduces enemies health by the current attack strenght of the player
* use potion - increases players health bar by 50 points and reduces healing potion count by 1
Battle continues until either player or enemie dies.
Once the enemy is killed player will gain fixed amout og gold and 1 health potion.

![image](https://github.com/SimasJakubenas/rpg-game-pp3/assets/138577499/aba70387-aab1-4299-b88b-01ab53f67478)

#### Item drop
7

After battle the player has a small chance to aquire(7) a weapon.

![image](https://github.com/SimasJakubenas/rpg-game-pp3/assets/138577499/0a798594-006e-4908-b496-bc12df1d4e8a)

#### Boss Fight
8

When the boss(8) is located and defeated game winning title is displayed and player is prompted with a choice to quit or continue playing.

### Future Features
15, 16, 19, 20, 21

There's many ways in which the game content can be expanded. Game enemy and item list can be increased by updating the worksheets. Same is true for the map size.
These area the features I decided to introduce in the near future:
* playable character selection(15)
* introduction of game difficulty levels(16)
* add music(19) and sound effects(20) to the game
* add ASCIi art to display encountered enemies

## Technologies Used

### Languages Used 

Python and it's libraries:
Random
Os
Gspread

### Frameworks, Libraries & Programs Used

- [Codeanywhere](https://dashboard.codeanywhere.com/) - used to write code at the start of developement
- [Gitpod](https://www.gitpod.io/) - used to write code later on 
- [Git](https://git-scm.com/) - for version control.
- [Lucid](https://www.lucidchart.com/) - used to create flowcharts
- [Git](https://git-scm.com/) - for version control.
- [GitHub](https://github.com/) - to save and store the files for the website
- [ASCII art generator](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=) - to create game title, win game and game over messages
- [README editor](https://readme.so/editor) - to help in readme writting
- [W3Schools](https://www.w3schools.com/) - for variaus python functionality querries
- [CI Python Linter](https://pep8ci.herokuapp.com/) - to validate python code
- [Heroku](https://dashboard.heroku.com/) - to deploy the project

## Deployment & Local Development

The site is deployed using Heroku Pages. Visit the deployed site [here](https://tal-rasha-rpg-6583f66e1480.herokuapp.com/).

### To deploy using Heroku

1 - On the Heroku website, navigate to dashboard and then click on the new button in the top right corner choosing: create new app.

2 - Type in a name for your app (this name will need to be unique) and choose a region for where you are located. Click create app.

3 - Your app has been created, now click on the settings tab.

4 - Click reveal config vars to add any keys the application will need. The api credentials for a spreadsheet access was used in this project.

5 - Click add buildpack to install interdependecies that are needed for the project. Like 'python' and 'nodejs'.

6 - Click on deploy tab. Select deploy method, in this case Git Hub. Fint the right repository and then connecting to it.

7 - To manually deploy project click 'Deploy Branch' in the deployment section. Once built click the view button to view the deployed page making a note of it's url.
