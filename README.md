# sudoku_solver
A primitive sodoku solver. Will solve most "easy" puzzles.

Will check each unfilled square for its allowed values as determined by the contents of its row, column and 3x3 square and fill in the value if the union of all three is one single value.

This is enough to solve easy puzzles, but cannot solve harder puzzles which depends on inspecting each row, column and 3x3 for the allowed values of each member, and then comparing them.

### Output

[4, 2, 3, 5, 9, 7, 1, 6, 8]
[1, 7, 9, 6, 4, 8, 3, 5, 2]
[6, 5, 8, 1, 2, 3, 9, 4, 7]
[3, 1, 5, 4, 6, 2, 8, 7, 9]
[2, 9, 7, 3, 8, 5, 6, 1, 4]
[8, 4, 6, 9, 7, 1, 5, 2, 3]
[7, 6, 4, 8, 1, 9, 2, 3, 5]
[5, 8, 1, 2, 3, 4, 7, 9, 6]
[9, 3, 2, 7, 5, 6, 4, 8, 1]

Solved Sudoku in 8 iterations!
