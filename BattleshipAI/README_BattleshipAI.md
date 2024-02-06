# Battleship Game and AI Strategy

## Overview
This Python script simulates a simplified version of the Battleship game and includes tools to analyze ship placements. The script also lays the foundation for implementing an AI that will find the best ship placements and develop optimal strategies for hitting other ships.

## Prerequisites
- Python 3.x
- Install required libraries using:
  ```bash
  pip install numpy
  pip install sympy
  pip install matplotlib
  pip install datascience
  ```

## Usage
1. Run the script by executing the following command:
   ```bash
   python battleship_game.py
   ```
2. The script will generate ship placements, test fairness of ship placements, and display a heatmap of ship placements.

## Code Explanation
- The script utilizes the `numpy`, `random`, `sympy`, `matplotlib`, and `datascience` libraries.
- The Battleship game is simulated with functions for horizontal and vertical ship placements, ship fairness testing, and distribution analysis.
- Ship placements are analyzed for fairness using horizontal and vertical distribution testing.
- The script generates a heatmap of ship placements on the game board.
- The script sets the groundwork for future implementation of an AI that will find optimal ship placements and strategies for hitting other ships.
