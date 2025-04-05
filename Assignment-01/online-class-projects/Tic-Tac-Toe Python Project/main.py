board = [' ']*9

def show_board():
    print(f"\n{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}\n")

def check_winner(p):
    win_cond = [(0,1,2),(3,4,5),(6,7,8),
                (0,3,6),(1,4,7),(2,5,8),
                (0,4,8),(2,4,6)]
    return any(board[a]==board[b]==board[c]==p for a,b,c in win_cond)

def play():
    current = 'X'
    for turn in range(9):
        show_board()
        move = int(input(f"Player {current}, choose (0-8): "))
        if board[move] != ' ':
            print("Invalid! Try again.")
            continue
        board[move] = current
        if check_winner(current):
            show_board()
            print(f"Player {current} wins!")
            return
        current = 'O' if current == 'X' else 'X'
    show_board()
    print("It's a draw!")

play()
