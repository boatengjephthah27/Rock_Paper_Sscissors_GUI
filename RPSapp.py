import tkinter as tk
from tkinter import ttk
import random as ran



app = tk.Tk()
app.title("Rock Paper Scissors")
app.iconbitmap("./Assets/RPS_logo.ico")
# style = Style()
# style.theme_names()
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
window_height = 750
window_width = 883
width_center = int(screen_width/2 - window_width/2)
height_center = int(screen_height/2 - window_height/2)
window_position = app.geometry(f"{window_width}x{window_height}+{width_center}+{height_center}")
app.resizable(False, False)

# adding images
win = tk.PhotoImage(file="./Assets/won.png")
lost = tk.PhotoImage(file="./Assets/lost.png")
draw = tk.PhotoImage(file="./Assets/draw.png")
prock = tk.PhotoImage(file="./Assets/player_rock.png")
ppaper = tk.PhotoImage(file="./Assets/player_paper.png")
pscissors = tk.PhotoImage(file="./Assets/player_scissors.png")
comrock = tk.PhotoImage(file="./Assets/com_rock.png")
compaper = tk.PhotoImage(file="./Assets/com_paper.png")
comscissors = tk.PhotoImage(file="./Assets/com_scissors.png")


# Defining front page
photo = tk.PhotoImage(file="./Assets/RPS_logo.png")
label = ttk.Label(app, image=photo)
# label.grid(row=0, column=0)
label.pack()


# building functions for the buttons
def choiceRock(event):
    pass


def choicePaper(event):
    pass


def choiceScissors(event):
    pass



#building the second page from continue button
def nextpage():
    c_names = ["Siri", "Bixbi", "Cortana", "Jarvis", "Friday", "Jexi", "Data", "Bishop", "C3PO", "R2D2", "Ava", "T-800", "Alexa"]   
    comp_name = ran.choice(c_names)
    playpage = tk.Toplevel()
    playpage.iconbitmap("./Assets/RPS_logo.ico")
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    window_height = 750
    window_width = 883
    width_center = int(screen_width/2 - window_width/2)
    height_center = int(screen_height/2 - window_height/2)
    window_position = playpage.geometry(f"{window_width}x{window_height}+{width_center}+{height_center}")
    # playpage.resizable(False, False)

    # make your choice label
    msglabel = tk.Label(playpage, text=".....MAKE A CHOICE.....", font=("Bungee Outline", "36", "bold"))
    msglabel.grid(row=0, column=1)
    space = ttk.Label(playpage, text="  ")
    space.grid(row=1)
    space = ttk.Label(playpage, text="  ")
    space.grid(row=2)
    plabel = tk.Label(playpage, text=f"Player: {p_name}", font=("Georgia", "20", "bold"))
    outlabel = tk.Label(playpage, text="Outcome: ", font=("Georgia", "20", "bold"))
    clabel = tk.Label(playpage, text=f"Computer: {comp_name}", font=("Georgia", "20", "bold"))
    plabel.grid(row=3, column=0)
    outlabel.grid(row=3, column=1)
    clabel.grid(row=3, column=2)

    space = ttk.Label(playpage, text="  ")
    space.grid(row=4)
    space = ttk.Label(playpage, text="  ")
    space.grid(row=5)
    # creating the graphics outputs
    pgraphics = ttk.Label(playpage, image=pscissors)
    pgraphics.grid(row=6, column=0, rowspan=1)
    outgraphics = ttk.Label(playpage, image=draw)
    outgraphics.grid(row=6, column=1, rowspan=1)
    cgraphics = ttk.Label(playpage, image=comscissors)
    cgraphics.grid(row=6, column=2, rowspan=1)
    space = ttk.Label(playpage, text="  ")
    space.grid(row=7)
    spac = ttk.Label(playpage, text="  ")
    spac.grid(row=8)

    # creating the RPS buttons
    rbutton = tk.Button(playpage, text="Rock", font=("Arial Black", "26", "bold"))
    rbutton.grid(row=9, column=0)
    pbutton = tk.Button(playpage, text="Paper", font=("Arial Black", "26", "bold"))
    pbutton.grid(row=9, column=2)
    sbutton = tk.Button(playpage, text="Scissors", font=("Arial Black", "26", "bold"))
    sbutton.grid(row=10, column=1)
    spac = ttk.Label(playpage, text="  ")
    spac.grid(row=11)
    spac = ttk.Label(playpage, text="  ")
    spac.grid(row=12)
    spac = ttk.Label(playpage, text="  ")
    spac.grid(row=13)
    spac = ttk.Label(playpage, text="  ")
    spac.grid(row=14)
    spac = ttk.Label(playpage, text="  ")
    spac.grid(row=14)
    spac = ttk.Label(playpage, text="  ")
    spac.grid(row=15)
    signature = ttk.Label(playpage, text="© App by: Boateng Jephthah Agyenim", font=("Signatura","7"))
    signature.grid(row=16, column=1)

    # binding keys to the buttons
    rbutton.bind("<R>", choiceRock)
    rbutton.bind("<r>", choiceRock)
    pbutton.bind("<P>", choicePaper)
    pbutton.bind("<p>", choicePaper)
    sbutton.bind("<S>", choiceScissors)
    sbutton.bind("<s>", choiceScissors)


    


# creating the name entry key binding function for <Return key>
def npage(event):
    nextpage()
    
# creating the name and entry widget 
nameFrame = ttk.Frame(app)
name = ttk.Label(nameFrame, text="Player Name: ", font=("Times New Roman", "18", "bold"))
name_entry = tk.Entry(nameFrame, font=("Times New Roman", "20"), borderwidth=3, width=40, bg="black", fg="white")
name.grid(row=0, column=0)
name_entry.grid(row=2, column=0)
nameFrame.pack()
name_entry.bind('<Key-Return>', npage)
p_name = name_entry.get()

# creating the continue button
continueButton = ttk.Button(text="Continue", command=nextpage)
continueButton.pack()

# creating my signature
sign = ttk.Label(app, text="© App by: Boateng Jephthah Agyenim", font=("Signatura","7"))
sign.pack()





























































app.mainloop()
