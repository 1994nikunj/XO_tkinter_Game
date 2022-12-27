from tkinter import Button, Entry, Label, Tk


class TicTacToe:
    def __init__(self, root):
        self.player_1 = 'X'
        self.stop_game = False

        self.button = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.states = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        root.title("Tic-Tac-Toe")
        root.resizable(0, 0)
        root.configure(bg='#202124')

        # ====================================================== Label: Heading
        label_top = Label(root, text="Enter your name to begin!", pady=10, padx=5)
        label_top.configure(bg='#202124', fg='#8ab4f8', font=("Consolas", 15, 'bold'))
        label_top.grid(row=0, column=0, columnspan=3)

        # ====================================================== Label + Input: Player 1
        label_player_1 = Label(root, text="PLAYER 1:")
        label_player_1.configure(bg='#202124', fg='#8ab4f8', font=("Consolas", 12, 'bold'))
        label_player_1.grid(row=1, column=0, columnspan=1)
        self.player_1_name = Entry(root)
        self.player_1_name.configure(bg='#575757', fg='#ffffff', font=("Consolas", 12))
        self.player_1_name.grid(row=1, column=1, columnspan=2)

        # ====================================================== Label + Input: Player 2
        label_player_2 = Label(root, text="PLAYER 2:")
        label_player_2.configure(bg='#202124', fg='#8ab4f8', font=("Consolas", 12, 'bold'))
        label_player_2.grid(row=2, column=0, columnspan=1)
        self.player_2_name = Entry(root)
        self.player_2_name.configure(bg='#575757', fg='#ffffff', font=("Consolas", 12))
        self.player_2_name.grid(row=2, column=1, columnspan=2)

        # ====================================================== Buttons: X / O
        for row in range(3):
            for col in range(3):
                self.button[row][col] = Button(
                    height=2, width=6,
                    font=("Consolas", 20, 'bold'),
                    command=lambda r=row, c=col: self.click_even(r, c))
                self.button[row][col].grid(row=row + 3, column=col)
                self.button[row][col].configure(bg='#303134', fg='#ec4e20')

        # ====================================================== Label: Winner
        self.label_winner = Label(root, text="Player 1's Turn", pady=10)
        self.label_winner.configure(bg='#202124', fg='#c58af9', font=("Consolas", 15, 'bold'))
        self.label_winner.grid(row=6, column=0, columnspan=3)

        restart = Button(root, text="Restart", command=self.restart)
        restart.grid(row=7, column=0, columnspan=3)
        restart.configure(bg='#2b2b2b', fg='#ec4e20', font=("Consolas", 15))

    def restart(self):
        self.player_1 = 'X'
        self.stop_game = False
        self.button = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.states = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        for row in range(3):
            for col in range(3):
                self.button[row][col] = Button(
                    height=2, width=6,
                    font=("Consolas", 20, 'bold'),
                    command=lambda r=row, c=col: self.click_even(r, c))
                self.button[row][col].grid(row=row + 3, column=col)
                self.button[row][col].configure(bg='#303134', fg='#ec4e20')

        self.label_winner.configure(text="Player 1's Turn")

    def click_even(self, r, c) -> None:
        if self.player_1 == "X" and self.states[r][c] == 0 and not self.stop_game:
            self.button[r][c].configure(text="X")
            self.states[r][c] = self.player_1_name.get()
            self.label_winner.configure(text="Player 2's Turn")
            self.player_1 = "O"

        if self.player_1 == 'O' and self.states[r][c] == 0 and not self.stop_game:
            self.button[r][c].configure(text='O')
            self.states[r][c] = self.player_2_name.get()
            self.label_winner.configure(text="Player 1's Turn")
            self.player_1 = "X"

        self.win_condition()

    def win_condition(self) -> None:
        win_bg = '#359c65'
        win_fg = '#303134'
        for i in range(3):
            if self.states[i][0] == self.states[i][1] == self.states[i][2] != 0:
                self.stop_game = True
                self.button[i][0].configure(bg=win_bg, fg=win_fg)
                self.button[i][1].configure(bg=win_bg, fg=win_fg)
                self.button[i][2].configure(bg=win_bg, fg=win_fg)
                self.label_winner.configure(text="WINNER: " + self.states[i][0])
                break

            elif self.states[0][i] == self.states[1][i] == self.states[2][i] != 0:
                self.stop_game = True
                self.button[0][i].configure(bg=win_bg, fg=win_fg)
                self.button[1][i].configure(bg=win_bg, fg=win_fg)
                self.button[2][i].configure(bg=win_bg, fg=win_fg)
                self.label_winner.configure(text="WINNER: " + self.states[0][i])
                break

            elif self.states[0][0] == self.states[1][1] == self.states[2][2] != 0:
                self.stop_game = True
                self.button[0][0].configure(bg=win_bg, fg=win_fg)
                self.button[1][1].configure(bg=win_bg, fg=win_fg)
                self.button[2][2].configure(bg=win_bg, fg=win_fg)
                self.label_winner.configure(text="WINNER: " + self.states[0][0])
                break

            elif self.states[0][2] == self.states[1][1] == self.states[2][0] != 0:
                self.stop_game = True
                self.button[0][2].configure(bg=win_bg, fg=win_fg)
                self.button[1][1].configure(bg=win_bg, fg=win_fg)
                self.button[2][0].configure(bg=win_bg, fg=win_fg)
                self.label_winner.configure(text="WINNER: " + self.states[0][2])
                break

            elif self.states[0][0] and self.states[0][1] and self.states[0][2] and self.states[1][0] and \
                    self.states[1][1] and self.states[1][2] and self.states[2][0] and self.states[2][1] and \
                    self.states[2][2] != 0:
                self.stop_game = True
                self.label_winner.configure(text="It's a TIE!")
                break


if __name__ == "__main__":
    try:
        window = Tk()
        TicTacToe(window)
        window.resizable(False, False)
        window.mainloop()
    except KeyboardInterrupt:
        exit()
