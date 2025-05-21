# Ruby Cave Game

A simple Python game where players collect rubies from a cave while avoiding traps. The game is designed to be easy to understand and modify.

## Project Structure

```
.
├── constants.py           # Game settings and card definitions
├── main.py               # Main game entry point
├── models/               # Game objects
│   └── player.py        # Player class
├── strategies/           # Player strategies
│   └── strategies.py    # Different ways players can play
└── game/                # Game logic
    └── game_manager.py  # Main game controller
```

## How to Play

1. Run the game:
   ```
   python main.py
   ```

2. Enter the number of players when prompted

3. The game will play automatically with:
   - Player 1 using the Basic Strategy
   - Other players using the Random Strategy

## Game Rules

- The game has 5 rounds
- Each round, players can collect rubies from the cave
- Players must decide when to leave the cave:
  - If they leave safely, they keep their rubies
  - If they stay and a second trap appears, they lose all rubies
- The player with the most rubies at the end wins

## Card Types

1. Ruby Cards (numbers):
   - Give rubies to all active players
   - Extra rubies stay in the cave

2. Trap Cards:
   - First trap: No effect
   - Second trap: All active players lose their rubies

3. Relic Cards:
   - Special cards that give bonus points
   - Only the last player leaving gets the relics

## Code Structure

### Player Class (`models/player.py`)
- Manages player's rubies and status
- Tracks rubies in hand and in chest
- Handles leaving the cave

### Strategies (`strategies/strategies.py`)
1. Basic Strategy:
   - Makes decisions based on:
     - Number of cards played
     - Number of traps
     - Rubies on the ground

2. Random Strategy:
   - Makes simpler decisions based on:
     - Current rubies in hand
     - Number of cards left
     - Round number

### Game Manager (`game/game_manager.py`)
- Controls the game flow
- Manages rounds and turns
- Handles card effects
- Tracks scores

## How to Modify

1. To add a new strategy:
   - Create a new class in `strategies.py`
   - Add a `play` method that returns `True` to leave or `False` to stay

2. To change game rules:
   - Modify constants in `constants.py`
   - Update card handling in `game_manager.py`

3. To add new features:
   - Add new methods to the `Player` class
   - Update the `GameManager` to handle new features

## Example Strategy

```python
class MyStrategy:
    def play(self, mon_coffre, mon_sac, rubis_au_sol, id_manche, les_joueurs, tas_tri, defausse):
        # Leave if we have more than 10 rubies
        if mon_sac > 10:
            return True
        # Stay otherwise
        return False
``` 