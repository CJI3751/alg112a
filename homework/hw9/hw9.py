def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True

def solve_queens(board, row):
    if row == len(board):
        return True 
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row] = col
            if solve_queens(board, row + 1):
                return True
           
            board[row] = -1
    return False

def print_solution(board):
    n = len(board)
    for i in range(n):
        row = ""
        for j in range(n):
            if board[i] == j:
                row += "Q "
            else:
                row += ". "
        print(row)
    print("\n")

n = 8
board = [-1] * n

if solve_queens(board, 0):
    print_solution(board)
else:
    print("No solution")
