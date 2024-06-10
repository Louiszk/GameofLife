# Conway's Game of Life
## [https://gameoflife-hhgd.onrender.com](https://gameoflife-hhgd.onrender.com)

This project is a web-based implementation of Conway's Game of Life using Dash and Plotly. Users can interactively set the initial state of the game board and start the simulation to see how the cells evolve over time.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Credits](#credits)

## Overview

Conway's Game of Life is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It's a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. Players create an initial configuration and observe how it evolves.

## Features

- Interactive grid to set initial live cells.
- Start and stop the simulation.
- Visualization of the evolving generations of cells.
- Easy-to-use interface.

## Usage

1. Open your web browser and go to [Conway's Game of Life](https://gameoflife-hhgd.onrender.com).
2. Click on the grid to set the initial live cells. Click again on a cell to toggle its state (alive/dead).
3. Click the "Start" button to begin the simulation.
4. Watch how the cells evolve over time according to the rules of Conway's Game of Life.

## How It Works

### Rules

The game is played on a grid of cells, each of which can be alive or dead. The state of the grid evolves in steps, with the following rules:

1. **Birth**: A dead cell with exactly three live neighbors becomes a live cell.
2. **Survival**: A live cell with two or three live neighbors stays alive.
3. **Death**: In all other cases, a cell dies or remains dead.

### Implementation

- **Dash and Plotly**: Used to create the interactive web interface and visualize the grid.
- **Numpy**: Used for efficient grid manipulation and calculation of the next generation of cells.

### File Structure

- `app.py`: The main application file containing the Dash app, callbacks, and game logic.


## Credits

This application was fully written by GPT-4, the language model developed by OpenAI.

---

Enjoy playing Conway's Game of Life!
