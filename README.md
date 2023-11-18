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

In the table bellow i tried to extract requirements for the site from user and developer stories and match those requirements with a set of features. Moreover I tried to follow agile approach where project features were split into sprints allowing for an early deployment of the project with basic controls of the game running. This permits the user the ability to test the game while I work on the second sprint.

| Requirement | Feature | sprint |
| -- | -- | -- |
| A functioning and fun RPG type game (FTU_03, FTU_04, FTU_05, FTU_06, RU_03, SD_01) | A starting town | 1 |
| | A shop for items/potions | 2 |
| | A stash to store items | 3 |
| | A map progression through the game | 1/2 |
| | A change to encounter enemies while navigating the map | 1 |
| | Battle sequence | 1 |
| | Chance to aquire items after the fight | 2 |
| | Boss fight at the end to win the game | 2 |
| An intuitive game menu (FTU_02, RU_01) | Option to start the game| 1 |
| | Option to end the game | 1 |
| | Game rules | 2 |
| | Option to save/load the game | 3 |
| Game title window (FTU_01) | ASCII art for game title | 2 |
| | Greeting message | 1 |
| Character selection (RU_02, FTU_08) | Introduce different playable characters | 3 |
| Game difficulty level (RU_02, RU_04) | Introduce game difficulty selection | 3 |
| Utilising google sheets (SD_02) | Storing game content on google spreadsheets | 1 |
| Deployment on Heroku (SD_03) | Deployed on Heroku | 1 |
| Adding game sounds/ASCII art (FTU_07) | Add game music | 3 |
| | Add game sounds | 3 |
| | Add ASCII art to improve the visuals of the game | 3 |

### Structure Plane

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