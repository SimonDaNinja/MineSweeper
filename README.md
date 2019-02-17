# MineSweeper

This program uses windows system functions to:
1. clear the screen.
2. check for existence of directories and paths.
3. create directories.

Hence,If you want to run the code on a non-windows system,
you have to modify the functions "clear()" and "CompareToHighScore()".
You can also just remove them and the places they're used in.
If you remove "CompareToHighScore()", you lose the highscore functionality.
If you remove "clear", the screen won't be cleared between moves, making for 
a less seemless playing experience. But the basic functionality should still
work.

This program uses the following libraries:
1. numpy
2. random
3. os (see first section of README)
4. time
5. copy
