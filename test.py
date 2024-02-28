class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []

def create_minimax_tree(board, depth, is_maximizing_player):
    if depth == 0 or not any(" " in row for row in board):
        return Node(value=evaluate_game_state(board))

    node = Node()

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                new_board = [row.copy() for row in board]
                new_board[i][j] = "X" if is_maximizing_player else "O"
                child = create_minimax_tree(new_board, depth - 1, not is_maximizing_player)
                node.children.append(child)

    return node

def evaluate_game_state(board):
    # Check for a win
    winner = check_winner(board)
    if winner == "X":
        return 1  # Maximizing player (X) wins
    elif winner == "O":
        return -1  # Minimizing player (O) wins

    # Check for a tie
    if " " not in [cell for row in board for cell in row]:
        return 0  # It's a tie

    # No winner yet, return a neutral score
    return 0

def check_winner(board):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        # Check rows and columns
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]  # Winner in a row
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]  # Winner in a column

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]  # Winner in the main diagonal
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]  # Winner in the other diagonal

    return None  # No winner yet

def minimax(node, depth, is_maximizing_player):
    if depth == 0 or not node.children:
        return node.value

    if is_maximizing_player:
        max_eval = float('-inf')
        for child in node.children:
            eval_child = minimax(child, depth - 1, False)
            max_eval = max(max_eval, eval_child)
        return max_eval
    else:
        min_eval = float('inf')
        for child in node.children:
            eval_child = minimax(child, depth - 1, True)
            min_eval = min(min_eval, eval_child)
        return min_eval

# Example usage
initial_board = [
    ["X", "O", "X"],
    [" ", "X", "O"],
    ["O", " ", "X"]
]

depth_of_tree = 3
root = create_minimax_tree(initial_board, depth_of_tree, True)
best_move_value = minimax(root, depth_of_tree, True)
print("Best move value:", best_move_value)
