def is_safe(board, row, col):
    # Check if there's a queen in the same column
    for i in range(row):
        if board[i] == col:
            return False
    
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i] == j:
            return False
    
    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, 8)):
        if board[i] == j:
            return False
    
    return True

def solve_queens(board, row):
    if row >= 8:  # If all queens are placed, return True
        return True
    
    for col in range(8):
        if is_safe(board, row, col):
            board[row] = col  # Place queen at position (row, col)
            if solve_queens(board, row + 1):  # Recur for next row
                return True
            board[row] = -1  # Backtrack if placing at (row, col) doesn't lead to a solution
    
    return False

def print_solution(board):
    for row in range(8):
        line = ""
        for col in range(8):
            if board[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()

def solve_8_queens():
    board = [-1] * 8  # Initialize board with no queens placed
    if not solve_queens(board, 0):
        print("No solution exists")
    else:
        print_solution(board)

if __name__ == "__main__":
    solve_8_queens()
