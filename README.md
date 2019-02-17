# MineSweeper

An implementation of the classic game Minesweeper!
You can customize the grid dimensions and number of mines.
Tiles are revealed by typing in row and column numbers (as prompted -
it's quite self-explanatory when playing.)

Highscores are parameter specific - when you play on a 5x5 map with 3 mines,
your time will not be compared to the best time for playing on a 9x9 map with 10
mines. However, equivalent but different parameter settings are commensurable, so
playtimes for 5x10 maps and 10x5 maps with the same number of mines will both be
compared to the same best time.

This program uses windows system functions to:
1. clear the command window.
2. check for existence of directories and paths.
3. create directories.

Hence, if you want to run the code on a non-windows system,
you have to modify the functions "clear()" and "CompareToHighScore()" in Main.py.
You can also just remove them and the places they're used in.
If you remove "CompareToHighScore()", you lose the highscore functionality.
If you remove "clear", the screen won't be cleared between moves, making for 
a less seamless playing experience. But the basic functionality should still
work.

This program uses the following libraries:
1. numpy
2. random
3. os (see first section of README)
4. time
5. copy
