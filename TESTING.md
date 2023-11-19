
## Testing

### Automated testing

I used CI pyhon linter to test the code and get a bunch of 'line too long' notifications. A lot of it is text positioning related. The total count of these can be reduced I just ran out of time to try and position all the text again. I also get 'continuation line with same indent as next logical line' on line 390 and I wasn't able to clear that.

![image](https://github.com/SimasJakubenas/rpg-game-pp3/assets/138577499/57578921-ce78-495a-a843-d65dfca434bf)

### Manual testing

#### Input verification

Game menu
| Input | Expected Result | Pass/Fail |
| --- | --- | --- |
| 1. Start Game | selected option brings up verifiction question | Pass |
| 1. Start Game | when input confirmed starts game | Pass |
| 2. Save Game | selected option brings up verifiction question | Pass |
| 2. Start Game | when input confirmed saves game | Pass |
| 3. Load Game | selected option brings up verifiction question | Pass |
| 3. Load Game | when input confirmed loads game | Pass |
| 5. Quit Game | selected option brings up verifiction question | Pass |
| 3. Quit Game | when input confirmed terminates game | Pass |
| Game menu | wrong input brings up message declaring that | Pass |

Town zone
| Input | Expected Result | Pass/Fail |
| --- | --- | --- |
| 1. Sewers | selected option brings up verifiction question | Pass |
| 1. Dessert | selected option brings up verifiction question | Pass |
| Q. Open menu | selected option brings up verifiction question | Pass |
| Q. Open menu Game | when input confirmed opens menu | Pass |
| W. Open character info | selected option brings up verifiction question | Pass |
| W. Open character info | when input confirmed opens character info table | Pass |
| E. Open stash | selected option brings up verifiction question | Pass |
| E. Open stash | when input confirmed opens stash | Pass |
| W. Vendor | selected option brings up verifiction question | Pass |
| W. Vendor | when input confirmed opens menu | Pass |
| any other input | wrong input brings up message declaring that | Pass |

Vendor
| Input | Expected Result | Pass/Fail |
| --- | --- | --- |
| 1. Buy | selected option brings up verification question | Pass |
| 1. Buy | when input confirmed opens vendor buy menu | Pass |
| 2. Sell | selected option brings up verification question | Pass |
| 2. Sell | when input confirmed opens vendor sell menu | Pass |
| 3. Gossip | selected option brings up verification question | Pass |
| 2. Gossip | when input confirmed opens vendor gossip window | Pass |
| any other input | wrong input brings up message declaring that | Pass |

Enemy zone
| Input | Expected Result | Pass/Fail |
| --- | --- | --- |
| 1. Go north | selected option moves player one tile up on the map | Pass |
| 2. Go east | selected option moves player one tile to right on the map | Pass |
| 3. Go south | selected option moves player one tile down on the map | Pass |
| 4. Go west | selected option moves player one tile to left on the map | Pass |
| any other input | wrong input brings up message declaring that | Pass |

Battle
| Input | Expected Result | Pass/Fail |
| --- | --- | --- |
| 1. Attack | selected option diminishes enemy health by attak strenght of hero | Pass |
| 2. Heal | selected option moves increases enemy health by 50 if health potion present | Pass |
| 2. Heal | if no health potions present it's declared | Pass |
| any other input | wrong input brings up message declaring that | Pass |


Any other input confirmation not listed wasn't included due to time constrains. 
The game works flawlessly to my best knowledge.