def find_next_empty(puzzle):
    # finds
    
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
        
    return None, None
    
def solve_sudoku(puzzle):
    # solve sudoku using backtracking
    
    row, col = find_next_empty(puzzle) 
