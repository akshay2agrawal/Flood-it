# Flood-it

## Description

This project implements a Python version of the popular "Flood It" puzzle game.

- The player is given an n × n board of tiles where each tile is given one of m colors.
- Each tile is connected to up to four adjacent tiles in the North, South, East, and West directions.
- A tile is connected to the origin (the tile in the upper left corner) if it has the same color as the origin and there is a connected path to the origin consisting only of tiles of this color.
- A player does a move by choosing one of the m colors. After the choice is made, all tiles that are connected to the origin are changed to the chosen color.
- The game proceeds until all tiles of the board have the same color.

## Features

- Customizable board size and number of colors
- Automated solver using a greedy algorithm

## Installation

Clone this repository or download the source code:

```bash
git clone https://github.com/akshay2agrawal/Flood-it.git
```

## Usage

To run the game with the automated solver:

```python
python flood_it.py
```

This will create a game with default settings and solve it using the greedy algorithm.

## Customization

The game can be customised by modifying the parameters when creating a `FloodItGame` instance:

```python
game = FloodItGame(size=10, num_colors=5)
```

## Run Test cases

```python
python -m unittest test_flood_it_game.py

```

## Code Structure

- `FloodItGame`: Main game class that handles the game board and mechanics
- `flood_fill` : Uses DFS to traverse through all the nodes connected to the origin while updating them if they have the same color. Uses visited set to ensure that no redunduncy is present while traversing eliminating the problem of an infinite loop. If a color is matched for a tile, its neighbouring tiles are added in the stack. If not, then we move on with the remaining tiles in the stack until its empty.
- `count_connected` : This function counts the number of connected tiles of a given color, starting from a specific position (x, y) on the game board. It's used to determine how many tiles would be filled if we choose a particular color.
- `get_best_move`: Function that determines the best move according to the greedy strategy
- `greedy_solve`: Function that solves the game using the greedy algorithm
