
def setup_puzzle():
  # Return a valid sudoku puzzle to solve. Temporarily hardcoded, 
  # but this board can be modified and should still be solveable for any "easy" solveable board
  board = [
            [None, None, 3, None, None, None, 1, 6, None],
            [None, None, None, 6, 4, None, None, 5, 2],
            [None, 5, None, 1, 2, 3, None, None, None],
            [3, None, 5, None, None, 2, 8, None, 9],
            [None, 9, None, 3, None, 5, None, 1, None],
            [8, None, 6, 9, None, None, 5, None, 3],
            [None, None, None, 8, 1, 9, None, 3, None],
            [5, 8, None, None, 3, 4, None, None, None],
            [None, 3, 2, None, None, None, 4, None, None]
          ]
  return board

def get_square_bounds(index):
  # For a given value return the min and max bounds of the sudoku square
  # Every row/col is divied into three squares bounded by [0, 2], [3, 5] and [6, 9]
  if index <= 2:
    return [0, 1, 2]
  elif index <= 5:
    return [3, 4, 5]
  else:
    return [6, 7, 8]

def get_numbers_in_row(puzzle, row):
  # Return all numbers in row, removing None values from list
  return [num for num in puzzle[row] if num is not None]
  #return puzzle[row]

def get_numbers_in_column(puzzle, index):
  # Search each row at a given index (to traverse a column) and return all the non-None values 
  column_values = []

  for row in puzzle:
    column_values.append(row[index])
  
  return [num for num in column_values if num is not None]

def get_numbers_in_square(puzzle, row, col):
  # Return list of all numbers in current square for which the intersection of row and col resides
  existing_values = []

  row_bounds, col_bounds = get_square_bounds(row), get_square_bounds(col)

  for row_index in row_bounds:
    for col_index in col_bounds:
      existing_values.append(puzzle[row_index][col_index])

  return [num for num in existing_values if num is not None]


def valid_placements(puzzle, row, col):
  # For a given row and column index in the current puzzle, return all valid placements
  row_allowed = set(ALLOWED_VALUES) - set(get_numbers_in_row(puzzle, row))
  col_allowed = set(ALLOWED_VALUES) - set(get_numbers_in_column(puzzle, col))
  sq_allowed = set(ALLOWED_VALUES) - set(get_numbers_in_square(puzzle, row, col))

  mutually_valid = list(set.intersection(row_allowed, col_allowed, sq_allowed))

  return mutually_valid


def none_values_on_board(puzzle):
  # Count how many None values are currenty on the board
  none_count = 0
  for row in puzzle:
    for index in row:
      if index is None:
        none_count += 1

  return none_count


def validate_final_solution(puzzle, iterations):
  # Quick validation to ensure solution obeys 
  none_count = 0

  for row in puzzle:
    for value in row:
      if value == None: none_count += 1
  
  for row in puzzle:
    print row

  if none_count == 0:
    print "\nSolved Sudoku in %s iterations!\n" %(iterations)
  else:
    print "Could not proceed after %s iterations :(" %(iterations)


if __name__ == "__main__":

  ALLOWED_VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  puzzle = setup_puzzle()
  iterations = 0
  change_made = True

  while change_made:
    if none_values_on_board(puzzle) == 0: break
    change_made = False
    iterations += 1
    row_index = -1

    for row in puzzle:
      row_index += 1
      col_index = -1

      for col in row:
        col_index += 1

        if puzzle[row_index][col_index] is None:
          possible_numbers = valid_placements(puzzle, row_index, col_index)
          if len(possible_numbers) == 1:
            puzzle[row_index][col_index] = possible_numbers[0]
            change_made = True
        else:
          change_made = True

  validate_final_solution(puzzle, iterations)
