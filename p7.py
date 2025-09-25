import tkinter as tk
from tkinter import messagebox

def check_winner():
    winning_combos = [
        [0,1,2], [3,4,5], [6,7,8],   # rows
        [0,3,6], [1,4,7], [2,5,8],   # columns
        [0,4,8], [2,4,6]             # diagonals
    ]
    for combo in winning_combos:
        if (buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != ""):
            for idx in combo:
                buttons[idx].config(bg="lightgreen")  # highlight winning buttons
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            reset_game()
            return True
    # Check for a tie
    if all(button["text"] != "" for button in buttons):
        messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
        reset_game()
        return True
    return False

def button_click(index):
    if buttons[index]["text"] == "" and not winner[0]:
        buttons[index].config(text=current_player[0])
        winner[0] = check_winner()
        if not winner[0]:
            toggle_player()

def toggle_player():
    current_player[0] = "O" if current_player[0] == "X" else "X"
    label.config(text=f"Player {current_player[0]}'s turn")

def reset_game():
    for button in buttons:
        button.config(text="", bg="SystemButtonFace")
    current_player[0] = "X"
    winner[0] = False
    label.config(text=f"Player {current_player[0]}'s turn")

# Setup main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

current_player = ["X"]  # Using list to allow modification in nested funcs
winner = [False]

buttons = []
for i in range(9):
    btn = tk.Button(root, text="", font=("Arial", 24), width=5, height=2,
                    command=lambda i=i: button_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

label = tk.Label(root, text=f"Player {current_player[0]}'s turn", font=("Arial", 16))
label.grid(row=3, column=0, columnspan=3)

root.mainloop()
