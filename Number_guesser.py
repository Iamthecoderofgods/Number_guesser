from tkinter import *
import random

root = Tk()

number_label = Label(root, text="Guess a number 1-20:")
entry = Entry(root)
outcome_label = Label(root, text="Outcome:", font=("Arial", 10, "bold"))
numbers = list(range(1, 21))
output = Label(root, text="Press button when Ready")


def Guuess():
    try:
        player_choice = int(entry.get())
    except ValueError:
        output.config(text="Please enter a number")
        return

    computer_choice = random.choice(numbers)

    if player_choice == computer_choice:
        output.config(text="You chose the right number: " + str(computer_choice))
    elif player_choice<computer_choice:
        output.config(text="you lost your guess is lower than the computers the computer choice was: "+str(computer_choice))
    elif player_choice>computer_choice:
        output.config(text="you lost, your answer was greater than the computers. the computers choice was:  "+str(computer_choice))
    else:
        output.config(
            text="You lost. The number that the computer chose was: " + str(computer_choice)
        )


guess_btn = Button(root, text="Guess", command=Guuess)

number_label.grid(row=1, column=10)
entry.grid(row=1, column=11)
guess_btn.grid(row=1, column=13)
outcome_label.grid(row=2, column=2)
output.grid(row=3, column=3)

root.mainloop()