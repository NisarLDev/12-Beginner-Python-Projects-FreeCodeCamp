def find_next_empty(puzzle):
    # finds
    
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
        
    return None, None # if no spaces in the puzzle are empty (-1)
    
def solve_sudoku(puzzle):
    # solve sudoku using backtracking
    # our puzzle is a list of lists, where each inner list is a row in our sudoku puzzle
    # return whether a solution exists
    # mutates puzzle to be the solution (if solution exists)
    
    # step 1: choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle) 
