
import matplotlib
matplotlib.use("Agg")   

import matplotlib.pyplot as plt

import random
import matplotlib.pyplot as plt

def draw_board(board):
    plt.figure(figsize=(5,5))
    for i in range(1,3):
        plt.plot([0,3],[i,i], color='black')  
        plt.plot([i,i],[0,3], color='black')  
 
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                plt.text(j+0.5, 2.5-i, 'X', fontsize=50, ha='center', va='center', color='red')
            elif board[i][j] == 'O':
                plt.text(j+0.5, 2.5-i, 'O', fontsize=50, ha='center', va='center', color='blue')
    plt.xlim(0,3)
    plt.ylim(0,3)
    plt.axis('off')
    plt.show()

def check_winner(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]): return True
        if all([board[j][i] == player for j in range(3)]): return True
    if board[0][0] == board[1][1] == board[2][2] == player: return True
    if board[0][2] == board[1][1] == board[2][0] == player: return True
    return False


board = [[" "]*3 for _ in range(3)]
players = ["X", "O"]
game_over = False

while not game_over:
    for player in players:
        empty_cells = [(i,j) for i in range(3) for j in range(3) if board[i][j]==" "]
        if not empty_cells:
            print("Draw!")
            game_over = True
            break

        move = random.choice(empty_cells)
        board[move[0]][move[1]] = player
        print(f"{player} plays at {move}")
        draw_board(board) 

        if check_winner(board, player):
            print(f"{player} wins!")
            game_over = True
            break
    if game_over:
        break
