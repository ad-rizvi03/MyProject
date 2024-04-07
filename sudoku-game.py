def print_board(board):
    for row in board:
        print(" ".join(str(cell) if cell != 0 else "_" for cell in row))

def is_valid_move(board, row, col, num):
    # Check if the number is not already in the row
    if num in board[row]:
        return False
    
    # Check if the number is not already in the column
    for i in range(3):
        if board[i][col] == num:
            return False
    
    # Check if the number is not already in the 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    
    return True

def is_board_full(board):
    for row in board:
        if 0 in row:
            return False
    return True

def solve_sudoku(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                for num in range(1, 4):
                    if is_valid_move(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def main():
    board = [[0 for _ in range(3)] for _ in range(3)]
    print("Welcome to 3x3 Sudoku!")
    print("Enter the initial board state:")
    for i in range(3):
        row = input(f"Enter values for row {i + 1} (separated by spaces): ").strip().split()
        for j in range(3):
            if row[j].isdigit():
                board[i][j] = int(row[j])
    print("\nInitial Board State:")
    print_board(board)
    
    if solve_sudoku(board):
        print("\nSolved Sudoku:")
        print_board(board)
    else:
        print("\nNo solution exists for the given board.")

if __name__ == "__main__":
    main()
