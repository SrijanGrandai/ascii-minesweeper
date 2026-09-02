# Minesweeper
This project involves an implementation of the game minesweeper in python with a MySQL backend.
Features include:
  - Board display after every turn
  - Leaderboard
  - Timer (the games are timed)
  - Save game

Prerequisites
If you want to try running the game on your computer, you will have to install MySQL and connect it to python.
You can install MySQL here:
https://dev.mysql.com/downloads/installer/

To link python to MySQL, you will have to run this command in your command prompt:
pip install mysql-connector-python



Core Logic & Implementation

- This game uses lists to store the current state of the board (hidden, flagged and revealed cells). Cells are identified by pure numbers. The user enters coordinates in the form (x,y) and it is converted to pure numbers during processing.


- Recursive Zero-Cell Clearing: When a user reveals a cell containing 0 adjacent mines, opening surrounding safe tiles manually would be tedious. The selectzerocells() function checks all 8 adjacent directions (N, S, E, W, and diagonals) while accounting for edge and corner boundary constraints. If a neighboring cell also has zero adjacent mines, it recursively invokes showcell(), automatically expanding outward to clear connected blank zones until reaching a perimeter of numbered cells.

- How games are saved:
  - Runtime board lists (hiddencells, minecells, displayedcells, flagcells) and active timer counts are converted into string format and stored in MySQL tables. Upon loading a saved session via load(), the data is converted back into active Python lists, instantly restoring board layout, flag positions, mine locations, and exact elapsed time.
