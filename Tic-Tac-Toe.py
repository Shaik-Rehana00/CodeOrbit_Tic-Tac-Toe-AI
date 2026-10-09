# Tic-Tac-Toe with Simple AI using Minimax

board = [" " for _ in range(9)]


# Display the board
def display_board():
    print("\n")
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print()


# Check whether a player has won
def check_winner(player):
    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] == player:
            return True

    return False


# Check whether board is full
def is_draw():
    return " " not in board


# Minimax algorithm
def minimax(is_maximizing):
    
    if check_winner("O"):
        return 1

    if check_winner("X"):
        return -1

    if is_draw():
        return 0

    if is_maximizing:
        best_score = -1000

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"

                score = minimax(False)

                board[i] = " "

                best_score = max(best_score, score)

        return best_score

    else:
        best_score = 1000

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"

                score = minimax(True)

                board[i] = " "

                best_score = min(best_score, score)

        return best_score


# Computer's move
def computer_move():
    best_score = -1000
    best_move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"

            score = minimax(False)

            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = "O"


# Main game
print("================================")
print("       TIC-TAC-TOE AI")
print("================================")
print("You = X")
print("Computer = O")
print("Choose positions from 1 to 9")

while True:

    display_board()

    # Player's move
    try:
        position = int(input("Enter your position (1-9): ")) - 1
    except ValueError:
        print("Please enter a number!")
        continue

    if position < 0 or position > 8:
        print("Choose a number between 1 and 9.")
        continue

    if board[position] != " ":
        print("That position is already occupied!")
        continue

    board[position] = "X"

    # Check player win
    if check_winner("X"):
        display_board()
        print("You Win!")
        break

    # Check draw
    if is_draw():
        display_board()
        print(" It's a Draw!")
        break

    # Computer's move
    print("Computer is thinking...")
    computer_move()

    # Check computer win
    if check_winner("O"):
        display_board()
        print("Computer Wins!")
        break

    # Check draw
    if is_draw():
        display_board()
        print(" It's a Draw!")
        break
