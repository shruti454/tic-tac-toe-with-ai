import math

# Display board
def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")

# Check if there are moves left
def is_moves_left(board):
    for row in board:
        if " " in row:
            return True
    return False

# Evaluate board state
def evaluate(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return 10 if row[0] == "O" else -10
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return 10 if board[0][col] == "O" else -10
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return 10 if board[0][0] == "O" else -10
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return 10 if board[0][2] == "O" else -10
    return 0

# Minimax Algorithm
def minimax(board, depth, is_max):
    score = evaluate(board)

    if score == 10:
        return score - depth
    if score == -10:
        return score + depth
    if not is_moves_left(board):
        return 0

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    best = max(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = " "
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    best = min(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = " "
        return best

# Find best move for AI
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                move_val = minimax(board, 0, False)
                board[i][j] = " "
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move

# Game loop
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe! You are X, AI is O.")
    print_board(board)

    while True:
        # Human move
        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter col (0-2): "))
                if board[row][col] == " ":
                    board[row][col] = "X"
                    break
                else:
                    print("Cell already taken! Try again.")
            except:
                print("Invalid input! Enter numbers 0-2.")

        print_board(board)

        if evaluate(board) == -10:
            print("You win!")
            break
        if not is_moves_left(board):
            print("It's a draw!")
            break

        # AI move
        print("AI's move...")
        move = find_best_move(board)
        board[move[0]][move[1]] = "O"
        print_board(board)

        if evaluate(board) == 10:
            print("AI wins!")
            break
        if not is_moves_left(board):
            print("It's a draw!")
            break

tic_tac_toe()
