import random

from tkinter import *
from tkinter import messagebox
from tkinter.font import *

from game import Game
from rule import ALL_CHOICEES, CONVERT_CHOICE


def show_single_mode():

    def show_result(user_choise):
        system_choice = random.choice(ALL_CHOICEES)
        match = Game(user_choise, system_choice)
        if Game.winner_person() == user_choise:
            messagebox.showinfo(
                message=
                f"You Won\n\nYour Choice: {CONVERT_CHOICE[user_choise]}\nSystem Choice: {CONVERT_CHOICE[system_choice]}"
                )

        elif Game.winner_person() == system_choice:
            messagebox.showwarning(
                message=
                f"System Won\n\nYour Choice: {CONVERT_CHOICE[user_choise]}\nSystem Choice: {CONVERT_CHOICE[system_choice]}"
                )

        else:
            messagebox.showinfo(
                message=
                f"Draw\n\nYour Choice: {CONVERT_CHOICE[user_choise]}\n System Choice: {CONVERT_CHOICE[system_choice]}"
                )

        messagebox.showinfo(message=match.counter_winner())


    def rock():
        show_result('r')


    def scissor():
        show_result('s')


    def paper():
        show_result('p')

    
    def reset():
        Game.counter_p1 = 0
        Game.counter_p2 = 0
        

    

    window_2 = Tk()

    window_2.geometry("650x350")
    window_2.title("Start Game")

    window_2['bg'] = "#E491F2"

    my_font = Font(family='Helvatica' , size=20)
    my_font_2 = Font(family='Consolas' , size=15)

    label = Label(window_2, text="Choose One", font=my_font_2)
    label.grid(row=0, column=0, pady=12, padx=10, columnspan=3, sticky=W+E)
    label.config(bg='#90ee90')

    rock_buttun = Button(window_2, text="Rock", width=7, height=4, font=my_font,
                            command=rock)
    rock_buttun.grid(row=3, column=0, padx=35, pady=15)

    scissor_buttun = Button(window_2, text="Scissor", width=7, height=4, font=my_font,
                            command=scissor)
    scissor_buttun.grid(row=3, column=1, padx=35, pady=15)

    paper_buttun = Button(window_2, text="Paper", width=7, height=4, font=my_font,
                            command=paper)
    paper_buttun.grid(row=3, column=2, padx=35, pady=15)


    reset_buttun = Button(window_2, text="RESET", font=my_font_2, command=reset)
    reset_buttun.grid(row=5, column=1, padx=35, pady=15)

    window_2.mainloop()