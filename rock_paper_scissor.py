import random
from tkinter import *

from PIL import Image, ImageTk

# main window
root = Tk()
# to change the title
root.title("Rock-Paper-Scissor")
root.configure(background="white")
root.resizable(False, False)

# Defining images from folder
rock_user, paper_user, scissor_user = ImageTk.PhotoImage(Image.open(".\\Resources\\rock_user.png")), ImageTk.PhotoImage(Image.open(".\\Resources\\paper_user.png")), ImageTk.PhotoImage(
    Image.open(".\\Resources\\scissor_user.png"))
rock_computer, paper_computer, scissor_computer = ImageTk.PhotoImage(Image.open(".\\Resources\\rock_computer.png")), ImageTk.PhotoImage(
    Image.open(".\\Resources\\paper_computer.png")), ImageTk.PhotoImage(Image.open(".\\Resources\\scissor_computer.png"))

# inserting pictures
user_label,comp_label = Label(root, image=paper_user, background="white"),Label(root, image=scissor_computer, background="white")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

# scores
user_score,comp_score = Label(root, text=0, bg="white", fg="blue", font=100),Label(root, text=0, bg="white", fg="blue", font=100)
user_score.grid(row=1, column=3)
comp_score.grid(row=1, column=1)

# indicators
Label(root, font=50, text="User", bg="white").grid(row=0, column=3)
Label(root, font=50, text="Computer", bg="white").grid(row=0, column=1)

# messages
msg = Label(root, font=50, bg="white")
msg.grid(row=3, column=2)

imgcomp = {"rock": rock_computer, "paper": paper_computer, "scissor": scissor_computer}
imguser = {"rock": rock_user, "paper": paper_computer, "scissor": scissor_user}


# update message
def updatemessage(x):
    msg['text'] = x


# update user score
def updateuserscore():
    score = int(user_score["text"])
    score += 1
    user_score["text"] = str(score)


# update computer score
def updatecompscore():
    score = int(comp_score["text"])
    score += 1
    comp_score["text"] = str(score)


outputwin = {"rock": ("paper"), "paper": ("scissor"), "scissor": ("rock")}


# Check winner
def checkWin(user, comp):
    if user == comp:
        updatemessage("Oops! It's a tie.")


    elif comp in outputwin[user]:
        updatemessage("Computer Scored a point")
        updatecompscore()
    else:
        updatemessage("You Scored a point")
        updateuserscore()


# defining a function for updating choices
choice = ["rock", "paper", "scissor"]


def updatechoice(x):
    # updates choice for the computer
    comp_choice = random.choice(choice)
    comp_label.config(image=imgcomp[comp_choice])
    # updates choice for the user
    user_label.config(image=imguser[x])
    checkWin(x, comp_choice)


# buttons
Button(root, width=20, height=2, bg="black", fg="white", text="Rock", font="aero", command=lambda: updatechoice("rock")).grid(row=2, column=1)
Button(root, width=20, height=2, bg="black", fg="white", text="Paper", font="aero", command=lambda: updatechoice("paper")).grid(row=2, column=2)
Button(root, width=20, height=2, bg="black", fg="white", text="Scissor", font="aero", command=lambda: updatechoice("scissor")).grid(row=2, column=3)

root.mainloop()
