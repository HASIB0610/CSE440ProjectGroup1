from tictactoe_ai import minimax  # Import minimax from ai.py

def print_board(board):
    """Print the Tic Tac Toe board."""
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("---------")

def player_move(board, human_player):
    """Handle player's move input."""
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit():
            move = int(move) - 1
            if 0 <= move < 9 and board[move] == " ":
                board[move] = human_player
                break
            else:
                print("Invalid move! Cell occupied or out of range.")
        else:
            print("Invalid input. Please enter a number (1–9).")

def ai_move(board, ai_player, use_heuristic=False, cutoff = 6):
    """Make the AI choose the best move using minimax."""
    print("AI is thinking...")
    score, move = minimax(board, player=ai_player, use_heuristic=use_heuristic, cutoff = cutoff)
    if move is not None:
        board[move] = ai_player
    else:
        print("No valid moves left.")

