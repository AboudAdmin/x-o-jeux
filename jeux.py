import tkinter as tk
from tkinter import messagebox

def check_win(board, player):
    
    for i in range(3):
        if all(cell == player for cell in board[i]):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def on_click(row, col):
    global current_player, buttons, board

    if board[row][col] == " ":
        buttons[row][col].config(text=current_player)
        board[row][col] = current_player

        if check_win(board, current_player):
            messagebox.showinfo("نهاية اللعبة", f"اللاعب {current_player} فاز!")
            reset_game()
            return

        if all(board[i][j] != " " for i in range(3) for j in range(3)):
            messagebox.showinfo("نهاية اللعبة", "تعادل!")
            reset_game()
            return

        current_player = "O" if current_player == "X" else "X"

def reset_game():
    global current_player, buttons, board

    current_player = "X"
    board = [[" " for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=" ")

root = tk.Tk()
root.title("لعبة X O")

current_player = "X"
board = [[" " for _ in range(3)] for _ in range(3)]
buttons = [[None] * 3 for _ in range(3)]

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text=" ", font=("Arial", 20), width=5, height=2,
                                   command=lambda row=i, col=j: on_click(row, col))
        buttons[i][j].grid(row=i, column=j, padx=5, pady=5)

reset_button = tk.Button(root, text="إعادة اللعبة", font=("Arial", 12), command=reset_game)
reset_button.grid(row=3, column=1, pady=10)

root.mainloop()


