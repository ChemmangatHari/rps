from tkinter import *
from PIL import Image,ImageTk
from random import randint

#main window
root = Tk()
#to change the title
root.title("Rock-Paper-Scissor") 
root.configure(background="white")
root.resizable(False, False)


#Defining images from folder
rock_user        = ImageTk.PhotoImage(Image.open("c:/Users/LENOVO/Desktop/python/MiniProjects/RPS/rock_user.png"))
paper_user       = ImageTk.PhotoImage(Image.open("c:/Users/LENOVO/Desktop/python/MiniProjects/RPS/paper_user.png"))
scissor_user     = ImageTk.PhotoImage(Image.open("c:/Users/LENOVO/Desktop/python/MiniProjects/RPS/scissor_user.png"))
rock_computer    = ImageTk.PhotoImage(Image.open("c:/Users/LENOVO/Desktop/python/MiniProjects/RPS/rock_computer.png"))
paper_computer   = ImageTk.PhotoImage(Image.open("c:/Users/LENOVO/Desktop/python/MiniProjects/RPS/paper_computer.png"))
scissor_computer = ImageTk.PhotoImage(Image.open("c:/Users/LENOVO/Desktop/python/MiniProjects/RPS/scissor_computer.png"))


#inserting pictures
user_label = Label(root ,image = paper_user ,background="white")
comp_label = Label(root ,image = scissor_computer ,background="white")
comp_label.grid(row = 1 ,column = 0)
user_label.grid(row = 1 ,column = 4)

#scores
user_score = Label(root ,text = 0 ,bg="white" ,fg="blue" ,font=100)
comp_score = Label(root ,text = 0 ,bg="white" ,fg="blue" ,font=100)
user_score.grid(row = 1 ,column = 3)
comp_score.grid(row = 1 ,column = 1)

#indicators
user_indicator = Label(root ,font = 50 ,text = "User" ,bg = "white").grid(row = 0 ,column = 3)
comp_indicator = Label(root ,font = 50 ,text = "Computer" ,bg ="white").grid(row = 0 ,column = 1)

#messages
msg = Label(root ,font = 50 ,bg = "white")
msg.grid(row = 3,column = 2)

#update message
def updatemessage(x):
    msg['text'] = x




#update user score
def updateuserscore():
    score = int(user_score["text"])
    score += 1
    user_score["text"] = str(score)

#update computer score
def updatecompscore():
    score = int(comp_score["text"])
    score += 1
    comp_score["text"] = str(score)


#Check winner
def checkWin(user ,comp):
    if user == comp:
        updatemessage("Oops! It's a tie.")
    elif user == "rock":
        if comp == "scissor":
            updatemessage("You Scored a point!Computer lost.")
            updateuserscore()
        else:
            updatemessage("Computer scored a point!You lost")
            updatecompscore()
    elif user == "paper":
        if comp == "scissor":
            updatemessage("Computer scored a point!You lost.")
            updatecompscore()
        else:
            updatemessage("You scored a point!Computer lost.")
            updateuserscore()
    elif user == "scissor":
        if comp == "rock":
            updatemessage("Computer scored a point!You lost.")
            updatecompscore()
        else:
            updatemessage("You scored a point!Computer lost")
            updateuserscore()
    else:
        pass


#defining a function for updating choices
choice = ["rock" ,"paper" ,"scissor"]
def updatechoice(x):

    #updates choice for the computer
    comp_choice = choice[randint(0,2)]
    if comp_choice == "rock":
        comp_label.config(image = rock_computer)
    elif comp_choice == "paper":
        comp_label.config(image = paper_computer)
    else:
        comp_label.config(image = scissor_computer)


    #updates choice for the user
    if x == "rock":
        user_label.config(image = rock_user)
    elif x == "paper":
        user_label.config(image = paper_user)
    else:
        user_label.config(image = scissor_user)

    checkWin(x ,comp_choice)

#buttons
rock = Button(root ,width = 20 ,height = 2 ,bg = "black" ,fg = "white" ,text ="Rock" ,font="aero" ,command = lambda: updatechoice("rock")).grid(row = 2,column = 1)
paper = Button(root ,width = 20 ,height = 2 ,bg = "black" ,fg = "white" ,text ="Paper" ,font="aero" ,command = lambda: updatechoice("paper")).grid(row = 2,column = 2)
scissor = Button(root ,width = 20 ,height = 2 ,bg = "black" ,fg = "white" ,text ="Scissor" ,font="aero" ,command = lambda: updatechoice("scissor")).grid(row = 2,column =3)




root.mainloop()
