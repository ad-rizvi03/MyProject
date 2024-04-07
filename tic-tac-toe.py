import random

def print_board(board):
    """
    Function to print the Tic-Tac-Toe board.
    """
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Function to check if there's a winner.
    """
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

def is_board_full(board):
    """
    Function to check if the board is full.
    """
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def get_empty_cells(board):
    """
    Function to get a list of empty cells on the board.
    """
    empty_cells = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                empty_cells.append((row, col))
    return empty_cells

def computer_move(board):
    """
    Function to generate a move for the computer.
    """
    empty_cells = get_empty_cells(board)
    return random.choice(empty_cells)

def main():
    """
    Main function to play Tic-Tac-Toe.
    """
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # User's move
        while True:
            row = int(input("Enter row (1, 2, or 3): ")) - 1
            col = int(input("Enter column (1, 2, or 3): ")) - 1
            if board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("That cell is already taken! Try again.")
        
        print_board(board)
        winner = check_winner(board)
        if winner:
            print(f"Congratulations! {winner} wins!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break

        # Computer's move
        print("Computer's turn...")
        row, col = computer_move(board)
        board[row][col] = "O"

        print_board(board)
        winner = check_winner(board)
        if winner:
            print(f"Sorry! Computer wins!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
